
import cv2 as cv
img = cv.imread("C:\\Users\\dda1v23\\Documents\\Python photos\\cat1.jpg")
def rescaleFrame(frame, scale=0.60):#takes in a frame and a scale factor and returns a resized version of the frame
    # takes in a frame and a scale factor and returns a resized version of the frame
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)  # interpolation is a technique used to resize or scale
    # an image while preserving its details
# def changeResize(width,height):#takes in a width and a height and returns a resized version of the frame,
#     # works for only live videos
#     capture.set(3,width)
#     capture.set(4,height)
resized_image = rescaleFrame(img)
cv.imshow('image', resized_image) #display the resized image
cv.waitKey(0)
cv.destroyAllWindows()




#READING VIDEOS

# capture = cv.VideoCapture("C:\\Users\\dda1v23\\Videos\\python videos\\Dog.mp4")
# while True:
#     isTrue, frame = capture.read() #read the current frame
#
#     frame_resized = rescaleFrame(frame, scale=.2) #resize the frame
#
#
#     cv.imshow("video", frame) #display the current frame
#     cv.imshow("video_resized", frame_resized) #display the resized frame
#
#     if cv.waitKey(20) & 0xFF == ord('d'):  #stop the video from playing indefinitely & breaking out of the while loop        break
#  #release the capture point
#         capture.release()