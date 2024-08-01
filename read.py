import cv2 as cv

#READING IMAGES

# img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")

# cv.imshow("cat", cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg"))

#READING VIDEOS

capture = cv.VideoCapture("C:\\Users\\dda1v23\\Videos\\python videos\\Dog.mp4")
while True:
    isTrue, frame = capture.read() #read the current frame
    cv.imshow("video", frame) #display the current frame

    if cv.waitKey(20) & 0xFF == ord('d'):  #stop the video from playing indefinitely & breaking out of the while loop        break
 #release the capture point
        capture.release()


cv.destroyAllWindows() #destroy all windows

#cv.waitKey(0) #wait for a keypress  to complete before continuing

#RESIZE AND RESCALE IMAGES


