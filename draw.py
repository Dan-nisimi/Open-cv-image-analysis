import cv2 as cv
import numpy as np

# img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
# cv.imshow("cat", img)

#1. Create a blank image of the same size as the original image
blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint the blank image a certain color
# color = np.array([0, 255, 0], dtype='uint8')  # Green color
# blank[200:300, 300:400] = color  # Fill the entire image with the color and draw a red square
# cv.imshow("Green", blank)

#2. Draw a rectangle

# img: The image on which the rectangle is to be drawn.
# pt1: The top-left corner of the rectangle.
# pt2: The bottom-right corner of the rectangle.
# color: The color of the rectangle.
# thickness: The thickness of the rectangle's border.
#cv.rectangle(blank, (0,0), (250, 500), (0, 0, 255), thickness= -1)
                 #or
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness= -1)
# # cv.imshow("Rectangle", blank)
# #
#
#
# #3. Draw a circle
# #cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
#                     #or
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow("Circle", blank)
#
#
#
# #4. Draw a line
# cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)
#
# cv.imshow("Line", blank)
#

#5. How to write a text on an image

cv.putText(blank, "Hello World, i am Daniel", (0,255), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)
cv.imshow("Text", blank)

# Wait for a key press
cv.waitKey(0)