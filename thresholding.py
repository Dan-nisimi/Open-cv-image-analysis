import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#thresholding is a function that takes an image and a threshold value and returns a binary image.
# The threshold value must be between 0 and 255 or black and white.
img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat5.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#SIMPLE THRESHOLDING

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)


threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded Inverse", thresh_inv)


#ADAPTIVE THRESHOLDING
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 11, 2)
cv.imshow("Adaptive Thresholded", adaptive_thresh)

cv.waitKey(0)