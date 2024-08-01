import cv2 as cv
import numpy as np

#opencv allows you to split RGB images into its different
# components or its 3 color channels B, G and R

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

#to print the color channels of the image for blank

blue = cv.merge([b, blank, blank])
green = cv.merge([blank,g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

#visualize the shape of the image
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#we can merge the image into a single image by using cv.merge()
merged = cv.merge((b, g, r))
cv.imshow("merged image", merged)


cv.waitKey()
cv.destroyAllWindows()