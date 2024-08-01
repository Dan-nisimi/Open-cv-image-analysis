import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#histogram is used to find the number (or visualize the distribution) of pixels in the image.

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat5.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask = circle)
masked = cv.bitwise_and(img, img, mask = mask)

# mask = cv.bitwise_and(img, img, mask = circle)
cv.imshow("mask", masked)


#GRAYSCALE HISTOGRAM

# gray_hist = cv.calcHist([gray], [0], None, [256 ], [0, 256])
# cv.imshow("Gray", gray)
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

#COLOR HISTOGRAM
plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    histr = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()
cv.waitKey(0)