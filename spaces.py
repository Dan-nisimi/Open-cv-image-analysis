import cv2 as cv
import matplotlib.pyplot as plt

#color space is a mathematical representation of color, used to describe
# and compare colors.It defines a set of colors and their relationships to
# each other, and can be used to convert between different color representations.
#Note: open cv displays bgr color and matplotlib displays rgb color.
img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\nature.jpg")
cv.imshow("nature", img)

# plt.imshow(img)
# plt.show()

#1. BGR to GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
plt.title("BGR to GRAYSCALE")

#2. BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
plt.title("BGR to HSV")

#3. BGR to L * a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)
plt.title("BGR to LAB")

#4. BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)
plt.title("BGR to RGB")

#5. HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr", hsv_bgr)
plt.title("HSV to BGR")

#6. LAB to BGR
lab_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow("hsv_bgr", lab_bgr)
plt.title("LAB to BGR")



plt.imshow(rgb)
plt.show()




cv.waitKey(0)
cv.destroyAllWindows()