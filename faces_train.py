import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = 'C:\\Users\\dda1v23\\Documents\\Python photos\\train'
# p =[]
# for i in os.listdir(r'C:\\Users\\dda1v23\\Documents\\Python photos\\train'):
#     p.append(i)
# print(p)
haar_cascade = cv.CascadeClassifier("haar_face.xml")
features = []
labels = []
def create_train(): #This function will be used to train the face recognition model
    for person in people: #creates a loop that iterates through each person in the people list.
        path = os.path.join(DIR, person) #creates a variable called path and sets its value to the result of calling the os.path.join function, which combines the DIR variable
        # (which stores the path to the training images) and the current person's name.
        label = people.index(person) #creates a variable called label and sets its value to
        # the current person's index in the people list'

        for img in os.listdir(path): # line creates a loop that iterates through the images in the
            # current person's directory (stored in the path variable).
            img_path = os.path.join(path, img) # creates a variable called img_path and sets its value to the result
            # of calling the os.path.join function, which combines the path variable and the current person's name.'

            img_array = cv.imread(img_path) #: This line reads the current image using the cv.imread function and stores
            # the result in a variable called img_array
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) # This line converts the image to grayscale using the
            # cv.cvtColor function and stores the result in a variable called gray.



            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4) #detects faces in the image
# using the Haar cascade classifier and stores the result in a variable called

            for (x, y, w, h) in faces_rect: #creates a loop that iterates through the detected faces.


                faces_roi = gray[y:y + h, x:x + w] #extracts the ROI of the current face and stores it in a variable
# called faces_roi. The ROI is defined by the coordinates of the top-left corner (stored in the x and y variables)
# and the width and height of the ROI (stored in the w and h variables)
                features.append(faces_roi)
                labels.append(label)


create_train() #calls the create_train function, which executes the code in the loop.
print('Training..........done')
# print(f'length of features: {len(features)}')
# print(f'length of labels: {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recognizer on the features list and labels list
face_recognizer.train(features, np.array(labels))

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)

np.save('labels.npy', labels)
