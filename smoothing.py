import cv2 as cv
import numpy as np

#opencv allows you to split RGB images into its different
# components or its 3 color channels B, G and R

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
cv.imshow("cat", img)

#1. AVERAGING BLUR

average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

#2. GAUSSIAN BLUR

gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gaussian)

#3. MEDIAN BLUR - BETTER AT REMOVING NOISE

median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

#4. BILATERAL BLUR

bilateral = cv.bilateralFilter(img, 5, 35, 15)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
cv.destroyAllWindows()




cv.waitKey(0)
cv.destroyAllWindows()