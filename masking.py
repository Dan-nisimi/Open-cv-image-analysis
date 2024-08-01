import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat5.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank Image", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow("mask", mask)

rectangle = cv.rectangle(blank.copy(), (30, 30), (300, 300), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)

# masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)


cv.waitKey(0)

