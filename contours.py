import cv2 as cv
import numpy as np


img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)
#
canny = cv.Canny(img, 125, 175) #canny edges detection
cv.imshow("canny", canny)

                #or use threshold where each pixel is assigned a value of 0 or 1
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #threshold binarizes the image
cv.imshow("Thresh", thresh)
#contours, hirerarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours, hirerarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#cv.CHAIN_APPROX_SIMPLE
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Contours Drawn", blank)

#contours and edges are kind of the same

cv.waitKey(0)
cv.destroyAllWindows()