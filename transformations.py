import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
cv.imshow("cat", img)

#1. TRANSLATION
#defined as Image translation is the process of moving an image in a certain direction (x, y) while preserving its content

def translate(img, x, y):
    # x, y is the number of pixels to move in the x and y direction respectively
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
#-x ---> Left coordinate
#-y ---> Top coordinate
#x ---> Right coordinate
#y ---> Bottom coordinate

translated = translate(img,-100,100)
cv.imshow("translated", translated)


#2. ROTATION
def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width / 2, height / 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow("rotated", rotated)

#rotate the rotated image
rotated_rotated = rotate(rotated, -90)
cv.imshow("Rotated Rotated", rotated_rotated)


#3. RESIZING
resized = cv.resize(img,(500, 400), interpolation=cv.INTER_LINEAR)
cv.imshow("resized", resized)

#4. FLIPPING
flip = cv.flip(img, 1)
cv.imshow("flip", flip)

cv.waitKey(0)
cv.destroyAllWindows()

#5. CROPPING
crop = img[100:300, 100:300]
cv.imshow("crop", crop)

cv.waitKey(0)
cv.destroyAllWindows()







cv.waitKey(0)
cv.destroyAllWindows()


