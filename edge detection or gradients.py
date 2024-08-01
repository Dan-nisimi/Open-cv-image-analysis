import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Laplacian operator works by taking the difference between adjacent pixels in an image
# (for example, pixel (x,y) and pixel (x+1,y)) and then smoothing those
# differences to create a more detailed edge map.

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat5.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


#LAPLACIAN

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#SOBEL

#sed for edge detection. It is a low-level operation that works by convolving the
# image with a kernel that detects edges based on the gradient of the image.
#Sobel operator calculates the gradient in two directions (x-axis and y-axis) and then combines the two results
# to create a more detailed edge map

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

#combined sobel operator is equivalent to sobelx + sobely

combined_sobel = cv.bitwise_or(sobelx, sobely)


cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)


#Canny Edge Detectors

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)