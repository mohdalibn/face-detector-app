
"""

    PROJECT: Face Detector App
    MADE BY: Mohd Ali Bin Naser
    GITHUB : github.com/mohdalibn

"""

# Importing the Libraries required for this project
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2


# Changes The Upload Button Image On Hover
def UploadBtnHover():
    pass


# Changes The Upload Button Image Off Hover
def UploadBtnLeave():
    pass


# Changes The Detect Button Image On Hover
def DetectBtnHover():
    pass


# Changes The Upload Button Image Off Hover
def DetectBtnLeave():
    pass


# Initializing Tkinter instanct
FaceDetectionApp = Tk()
FaceDetectionApp.title("Face Detection App")
FaceDetectionApp.geometry("800x550")  # Size of the tkinter window
# Added an Icon for the App
FaceDetectionApp.iconbitmap('AppImages/AppIcon.ico')
FaceDetectionApp.configure(bg="#fff")

# Creating a Canvas for the App
canvas = Canvas(FaceDetectionApp, bg="#ffffff", height=550,
                width=800, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Loading the Background Image of the App
background_img = PhotoImage(file=f"AppImages/background.png")
background = canvas.create_image(400.0, 275.0, image=background_img)


# Upload Image/Video Button
BtnImg1 = PhotoImage(file=f"AppImages/UploadImg.png")
UploadBtn = Button(
    image=BtnImg1,
    borderwidth=0,
    highlightthickness=0,
    bg="#000",
    cursor="hand2",
    relief="flat")

UploadBtn.place(
    x=55, y=164,
    width=244,
    height=44)

UploadBtn.bind("<Enter>", UploadBtnHover)
UploadBtn.bind("<Leave>", UploadBtnLeave)

# Detect Faces Button
BtnImg2 = PhotoImage(file=f"AppImages/DetectImg.png")
DetectBtn = Button(
    image=BtnImg2,
    borderwidth=0,
    highlightthickness=0,
    bg="#000",
    cursor="hand2",
    relief="flat")

DetectBtn.place(
    x=55, y=297,
    width=244,
    height=44)

DetectBtn.bind("<Enter>", DetectBtnHover)
DetectBtn.bind("<Leave>", DetectBtnLeave)


# Starting the Tkinter MainLoop
FaceDetectionApp.mainloop()
