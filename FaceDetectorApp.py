
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
def UploadBtnHover(e):
    # Initially, DetectionMode is zero
    if not VideoMode:
        hoverImg = PhotoImage(file=f"AppImages/HoverUploadImg.png")
    else:
        hoverImg = PhotoImage(file=f"AppImages/HoverVideoUploadImg.png")

    UploadBtn['image'] = hoverImg
    UploadBtn.image = hoverImg


# Changes The Upload Button Image Off Hover
def UploadBtnLeave(e):
    if not VideoMode:
        leaveImg = PhotoImage(file=f"AppImages/UploadImg.png")
    else:
        leaveImg = PhotoImage(file=f"AppImages/VideoUploadImg.png")

    UploadBtn['image'] = leaveImg
    UploadBtn.image = leaveImg


# Changes The Detect Button Image On Hover
def DetectBtnHover(e):
    hoverImg = PhotoImage(file=f"AppImages/HoverDetectImg.png")
    DetectBtn['image'] = hoverImg
    DetectBtn.image = hoverImg


# Changes The Upload Button Image Off Hover
def DetectBtnLeave(e):
    leaveImg = PhotoImage(file=f"AppImages/DetectImg.png")
    DetectBtn['image'] = leaveImg
    DetectBtn.image = leaveImg


ImageVar = ""  # Initializing the ImageVar Variable with Empty String
VideoVar = ""  # Initializing the VideoVar Variable with Empty String
# Variable to keep track of whether the Video Radio Button is Active or not
VideoMode = False
FaceCount = 0  # Variable to keep track of number of faces on an Image/Video Frame

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

# Adding Radio Buttons for the user to choose between Image Mode and Video Mode
DetectionMode = IntVar()
ImageRadBtn = Radiobutton(FaceDetectionApp, text=" IMAGE", font=('Helvatical bold', 12),
                          activebackground='black', activeforeground='#FF9393', bg="black", fg="#FF9393", value=1,
                          variable=DetectionMode, cursor='hand2', command=DetectMode)
VideoRadBtn = Radiobutton(FaceDetectionApp, text=" VIDEO", font=('Helvatical bold', 12), activebackground='black', activeforeground='#FF9393', bg="black",  fg="#FF9393", value=2,
                          variable=DetectionMode, cursor='hand2', command=DetectMode)

ImageRadBtn.place(x=82, y=115)
VideoRadBtn.place(x=187, y=115)


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

# Binding Functions for Hover Effect on the Upload Button
UploadBtn.bind("<Enter>", UploadBtnHover)
UploadBtn.bind("<Leave>", UploadBtnLeave)

# Label to Display the File Name that the user uploads
FileNameLabel = Label(FaceDetectionApp, bg="#C4C4C4",
                      text="File Name: No File Selected", font=('Helvatical bold', 15))
FileNameLabel.place(x=40, y=237)

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

# Binding Functions for Hover Effect on the Detect Button
DetectBtn.bind("<Enter>", DetectBtnHover)
DetectBtn.bind("<Leave>", DetectBtnLeave)

# Label to Display the Result
FaceCountLabel = Label(FaceDetectionApp, bg="#C4C4C4", text="Result: None",
                       font=('Helvatical bold', 15))
FaceCountLabel.place(x=40, y=370)

# Main Label For the Output Window
OutputWindowLabel = Label(FaceDetectionApp, bg="#000")
OutputWindowLabel.place(x=417, y=95)


# Starting the Tkinter MainLoop
FaceDetectionApp.mainloop()
