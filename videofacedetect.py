import cv2
import sys
from random import randrange

# STEPS
# 1. MAKE A CLASSIFIER
# 2. CHOOSE THE SOURCE OF IMAGE TO DETECT THE FACE IN. Ex- images, webcam
# 3. CONVERT THE IMAGE TO GRAY SCALE
# 4. PASS THE GRAY IMAGE TO THE HAAR CASCADE ALGORITHM
# 5. GET THE TOP LEFT COORDS AND THE WIDTH AND THE HEIGHT OF THE RECTANGLE
# 6. USE THE RECTANGLE FUNCTION TO DRAW A RECTANGLE USING THE COORDS, WIDTH, AND HEIGHT
# 7. DISPLAY THE WINDOW
# 8. USE THE WAITKEY() FUNCTION TO PAUSE THE EXECUTION OF THE CODE SO THAT WINDOW REMAINS OPEN


trained_faced_data = cv2.CascadeClassifier(
    './haarcascade_frontalface_default.xml')


# video = cv2.VideoCapture(0) # this line will use the webcam of the laptop
video = cv2.VideoCapture('./videos/DeliveryDriver.mp4')
#video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

# code for using the phone webcame using the ipwebcam app
# address = "http://192.168.1.104:8080/video"
# video.open(address)

# Videos are a collections of frames/pictures so we need to use a loop
while True:

    # Read the current frame of the video
    # the first variable is a boolean. It returns true if the frame was read successfully

    successfull_frame_read, frame = video.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    face_coordinates = trained_faced_data.detectMultiScale(grayscaled_frame)

    for cell in face_coordinates:

        x1, y1, width, height = cell
        cv2.rectangle(frame, (x1, y1), (x1 + width,
                      y1 + height), (0, 255, 0), 2)

    new_img = cv2.resize(frame, (640, 480))

    cv2.imshow("Frontal face detector", new_img)

    # '1' represents the time in milisecs this function waits on a single frame
    key = cv2.waitKey(1)

    if key == 81 or key == 113:  # 81 and 113 are the ascii values of the letter 'q'
        break


# print(face_coordinates)


# new_img = cv2.resize(img, (1000, 720))


print("Code has successfully completed!")
