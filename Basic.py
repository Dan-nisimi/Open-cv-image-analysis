import cv2 as cv

img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
cv.imshow("cat", img)

#1.CONVERT TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#2.BLUR
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) #kernel size is 7x7 and it should increase blur size
cv.imshow("Blur", blur)

#3.EDGE CASCADE
canny = cv.Canny(blur, 125, 125) #use blur instead of img to blur or reduce the edges
cv.imshow("Canny Edges", canny)

#4.DILATE IMAGES
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("Dilated", dilated)

#5. ERODED

eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow("Eroded", eroded)

#6. RESIZE IMAGES
resized = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

7. # CROPPING IMAGES
cropped = img[200:400, 200:400]
cv.imshow("Cropped", cropped)





cv.waitKey(0)
