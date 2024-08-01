import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (300, 300), 255, -1)
circle = cv.circle(blank.copy(),(200, 200),200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

#1. BITWISE AND ---> finds intersecting regions

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

#2. BITWISE OR ---> finds non-intersecting regions and intersecting regions

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

#3. BITWISE XOR ---> finds non-intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

#4. BITWISE NOT --->
    

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Rectangle Not", bitwise_not)

cv.waitKey(0)


cv.destroyAllWindows()
