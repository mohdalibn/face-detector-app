# Importing Libraries For the Project
import cv2
import sys
from random import randrange
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

# STEPS
# 1. MAKE A CLASSIFIER
# 2. CHOOSE THE SOURCE OF IMAGE TO DETECT THE FACE IN. Ex- images, webcam
# 3. CONVERT THE IMAGE TO GRAY SCALE
# 4. PASS THE GRAY IMAGE TO THE HAAR CASCADE ALGORITHM
# 5. GET THE TOP LEFT COORDS AND THE WIDTH AND THE HEIGHT OF THE RECTANGLE
# 6. USE THE RECTANGLE FUNCTION TO DRAW A RECTANGLE USING THE COORDS, WIDTH, AND HEIGHT
# 7. DISPLAY THE WINDOW
# 8. USE THE WAITKEY() FUNCTION TO PAUSE THE EXECUTION OF THE CODE SO THAT WINDOW REMAINS OPEN

# ALGORITHM EXPLAINATION
# Chain of events funneling down to where there is a face.
# Haar features - aka rudimentary building blocks
# Training the data - Supervised learning
#   Positive and negative images.in simple terms, they are just labels. example - faces and non  faces

# this loads some pre-trianed data on face frontals from opencv github repo (haar cascade algorithm)
# CascadeClassifier function is called to make a classifier. According to the vid, a classifier is used to classify an object. Eg - face
trained_faced_data = cv2.CascadeClassifier(
    './haarcascade_frontalface_default.xml')

# choose the image to detect the face in
img = cv2.imread('./images/rockandkevin.png')

# the next line converts the img to a grayscale image
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# passing the image to the haar cascade algorithm
# The classifier detects the face regardless of the scale of the image
face_coordinates = trained_faced_data.detectMultiScale(grayscaled_img)

# this line prints the top left corner and both right corner coords of the face
print(face_coordinates)

# the following lines loops over the list inside the face_coordinate and unpack the top left and the width and height of the rectangle
for cell in face_coordinates:  # this code is used to draw rectangles around multiple faces

    x1, y1, width, height = cell
    # opencv color format is bgr instead of rgb. '2' here is the thickness of the rectangle
    cv2.rectangle(img, (x1, y1), (x1 + width, y1 + height),
                  (0, randrange(256), 0), 2)


# Alternative method to get the coords, width and height
# (x1, y1, width, height) = face_coordinates[0]


# the following line prompts the display
new_img = cv2.resize(img, (640, 480))  # resized the size of the window
cv2.imshow("Frontal face detector", new_img)


# this line pauses the execution of the code until the specific key is pressed
cv2.waitKey()  # without this line, the prompt window will close instantly


print("Code has successfully completed!")
