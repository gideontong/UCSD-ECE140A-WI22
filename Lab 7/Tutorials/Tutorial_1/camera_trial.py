import cv2
cam = cv2.VideoCapture(0)
ret, image = cam.read()
cv2.imwrite('./test.jpg', image)
cam.release()
