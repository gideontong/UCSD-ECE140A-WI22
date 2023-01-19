import numpy as np
import cv2
import os

# Setting to camera capture to camera resolution 480 x 640
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:
    # Keep track of frames for debugging and image testing
    frames = 0

    if not os.path.exists("./Frames/"):
    os.mkdir("./Frames/")
    print("Created new directory for logging frames")

    # Start live feed
    while(frames >= 0):

        # Read with the USB camera
    _, frame = cap.read()

    frames += 1

    # Convert to hsv deals better with lighting
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red is on the upper and lower of hsv scale. Requires 2 ranges
    lower1 = np.array([0, 150, 20])
    upper1 = np.array([10, 255, 255])
    lower2 = np.array([160, 100, 20])
    upper2 = np.array([179, 255, 255])

    # Mask input image with upper and lower red ranges
    red_only1 = cv2.inRange(hsv, lower1, upper1)
    red_only2 = cv2.inRange(hsv, lower2, upper2)

    red_only = red_only1 + red_only2

    # Mask for kernel opening
    mask = np.ones((5, 5), np.uint8)

    # Opening operation on red_only for denoising
    opening = cv2.morphologyEx(red_only, cv2.MORPH_OPEN, mask)

    # Run connected components algo to return all objects it sees.
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        opening, 4, cv2.CV_32S)

    # Matrix showing labels for each pixel in the image
    b = np.matrix(labels)

    if num_labels > 1:
        # Extracts the label of the largest none background component
        # and displays distance from center and image.
        max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA])
                                  for i in range(1, num_labels)], key=lambda x: x[1])

        # Get only pixels with max_label as high (1), rest zero
        seg = (b == max_label)

        # Convert data to binary image
        seg = np.uint8(seg)
        seg[seg > 0] = 255

        # Get distance from center
        print('distance from center:', -1 * (320 - centroids[max_label][0]))

        # Log images for debugging
        cv2.imwrite(f"./Frames/data_{frames}.png", frame)
        cv2.imwrite(f"./Frames/seg_{frames}.png", seg)

    else:
        print("no object in view")
# To stop video execution, track exception and exit
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

