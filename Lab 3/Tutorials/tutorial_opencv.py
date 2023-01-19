import cv2

img1 = cv2.imread(“./images/geisel.jpg”) # Default condition or 1
print(img1.shape)  # (476, 640, 3)

img2 = cv2.imread(“./images/geisel.jpg”, 0) # Default condition
print(img2.shape)  # (476, 640)

cv2.imshow('Window Name', image) #Show image
c = cv2.waitKey(0) # Wait for termination key
cv2.destroyAllWindows() # Destroy all opened windows

cv2.imshow("GrayGeisel", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

sobelx = cv2.Sobel(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge

edge_canny = cv2.Canny(img1, 100, 200) #  
