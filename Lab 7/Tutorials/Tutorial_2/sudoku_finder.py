# Import OpenCV
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Read the image
image_url = "./sudoku_test.jpeg"
img = cv2.imread(image_url, 0)
# 0 is a simple alias for cv2.IMREAD_GRAYSCALE


# Preprocessing

# Add a Gaussian Blur to smoothen the noise
blur = cv2.GaussianBlur(img.copy(), (9, 9), 0)
cv2.imwrite("Blur.png", blur)

# Threshold the image to get a binary image
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imwrite("Threshold.png", thresh)

# Invert the image to swap the foreground and background
invert = 255 - thresh
cv2.imwrite("Inverted.png", invert)

# Dilate the image to join disconnected fragments
kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
dilated = cv2.dilate(invert, kernel)
cv2.imwrite("Dilated.png", dilated)
