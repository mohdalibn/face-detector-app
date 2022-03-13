
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


# Loading the Pre-Trained Haar Cascaade Face Model Using OpenCV
trained_faced_data = cv2.CascadeClassifier(
    './haarcascade_frontalface_default.xml')


# Destroys and Creates a New Output Label when a the Mode is changed or a new file is selected
def DestroyOutputLabel():
    global OutputWindowLabel

    # This removes and image/video on the Label when the Upload button is click
    OutputWindowLabel.destroy()
    OutputWindowLabel = Label(FaceDetectionApp, bg="#000")
    OutputWindowLabel.place(x=417, y=95)


def FilePrompt():
    global ImageVar, VideoVar, FaceCount

    # Setting the FaceCount to Zero each time the function is called
    FaceCount = 0

    # Executes when DetectionMode is set to Image
    if not VideoMode:
        FilePath = filedialog.askopenfilename(filetypes=[(
            "PNG Image File", "*.png"), ("JPG Image File", "*.jpg"), ("JPEG Image File", "*.jpeg")])

    # Executes when DetectionMode is set to Video
    else:
        FilePath = filedialog.askopenfilename(filetypes=[(
            "MP4 File", "*.mp4"), ("AVI File", "*.avi")])

    # Checks whether the length of the file path is greater than 0
    if len(FilePath) > 0:

        if not VideoMode:
            ImageVar = cv2.imread(FilePath)
        else:
            VideoVar = cv2.VideoCapture(FilePath)

        # Getting the Image Name From the Image File Path
        PathStr = FilePath
        PathStr = PathStr.split('/')
        FileName = PathStr[-1]

        # Update the Image File Name to Display
        FileNameLabel.configure(text="File Name: " + FileName)

        # Removing the Output Window Image/Video when a new image/video is chosen
        OutputWindowLabel.image = ""
        FaceCountLabel.configure(text="Result: None")

    else:
        FileNameLabel.configure(text="File Name: No File Selected!")

    # This removes and image/video on the Label when the Upload button is click
    DestroyOutputLabel()


# This function displays the face count on the FaceCountLabel using the FaceCount variable
def FaceCounter():
    global FaceCount

    if FaceCount > 0:
        if FaceCount == 1:
            FaceCountLabel.configure(
                text="Result: " + str(FaceCount) + " Face Detected!")
        else:
            FaceCountLabel.configure(
                text="Result: " + str(FaceCount) + " Faces Detected!")
    else:
        FaceCountLabel.configure(text="Result: No Faces Detected!")


def NewFrameSize(frame):
    height, width, channels = frame.shape
    ratio = height/width

    new_width = width
    new_height = height

    if height > 400 or width > 300:
        if ratio < 1:
            new_width = 300
            new_height = int(new_width * ratio)
        else:
            new_height = 400
            new_width = int(new_height * (width / height))

    ratio = height / new_height
    frame = cv2.resize(
        frame, (new_width, new_height))

    newImage = Image.fromarray(frame)
    FinalImage = ImageTk.PhotoImage(image=newImage)

    return FinalImage, new_width, new_height


# This function is executed when it is called through the FaceDetection function when the VideoMode is set to true
def PlayVideo():
    global VideoVar, FaceCount

    FaceCount = 0  # Initially setting FaceCount to 0 for each frame of a video so that sum doesn't add up the count of faces for all the frames played

    success, frame = VideoVar.read()

    if success == True:
        # frame = imutils.resize(frame, width=550)

        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

        face_coordinates = trained_faced_data.detectMultiScale(
            grayscaled_img)

        for cell in face_coordinates:  # this code is used to draw rectangles around multiple faces

            # Incrementing the Facecount
            FaceCount += 1

            x1, y1, width, height = cell

            # opencv color format is bgr instead of rgb. '2' here is the thickness of the rectangle
            cv2.rectangle(frame, (x1, y1), (x1 + width, y1 + height),
                          (0, 0, 255), 4)

            DisplayText = "Face " + str(FaceCount)

            cv2.putText(frame, DisplayText,
                        (x1 + (width//4), y1 + height + 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 0, 0), 5, cv2.LINE_AA)

        OutputImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        FinalFrame, _, _ = NewFrameSize(OutputImage)

        OutputWindowLabel.configure(image=FinalFrame)
        OutputWindowLabel.image = FinalFrame
        OutputWindowLabel.after(1, PlayVideo)

        # Updates the count of faces on the Result Label
        FaceCounter()


# This function is executed when the Detect Face Button is Clicked
def FaceDetection():
    global ImageVar, VideoVar, FaceCount, DetectionMode

    if not VideoMode and len(ImageVar) < 1:
        FileNameLabel.configure(text="File Name: Select An Image")

    elif FaceCount >= 1:  # This if statement prevents the user from spamming the Detect Face Button
        if not VideoMode:
            FaceCountLabel.configure(text="Result: Select a new image!")
        else:
            FaceCountLabel.configure(text="Result: Select a new video!")

    else:

        if VideoMode:

            _, frame = VideoVar.read()  # The purpose this line is to get the first frame of the video so that we can calculate and update the Black Output Label position just once instead of repeating it in the video loop

            # Unpacking the values returned by the function
            _, NewWidth, NewHeight = NewFrameSize(frame)

            # Updating the new Black Output Label Position
            LabelPositionCalc(NewWidth, NewHeight)

            PlayVideo()

        else:
            # Converting the Image to GrayScale
            grayscaled_img = cv2.cvtColor(ImageVar, cv2.COLOR_BGRA2GRAY)

            face_coordinates = trained_faced_data.detectMultiScale(
                grayscaled_img)

            for cell in face_coordinates:  # this code is used to draw rectangles around multiple faces

                # Incrementing the Facecount
                FaceCount += 1

                x1, y1, width, height = cell

                # opencv color format is bgr instead of rgb. '2' here is the thickness of the rectangle
                cv2.rectangle(ImageVar, (x1, y1), (x1 + width, y1 + height),
                              (0, 0, 255), 4)

                DisplayText = "Face " + str(FaceCount)

                cv2.putText(ImageVar, DisplayText,
                            (x1 + (width//4), y1 + height + 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 10, cv2.LINE_AA)

            OutputImage = cv2.cvtColor(ImageVar, cv2.COLOR_BGR2RGB)

            FinalImage, new_width, new_height = NewFrameSize(OutputImage)

            # Calculating the label position according to the frame size
            LabelPositionCalc(new_width, new_height)

            # Updating the SecondaryImgLabel to Display
            OutputWindowLabel.configure(image=FinalImage)
            OutputWindowLabel.image = FinalImage

            # Updates the count of faces on the Result Label
            FaceCounter()


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


# Function that Updates the App when either of the Modes are choosen
def DetectMode():
    global VideoMode

    DestroyOutputLabel()

    # Code to Change the image of the upload button if detection mode is video
    if DetectionMode.get() == 2:
        VideoMode = True
        VideoImg = PhotoImage(file=f"AppImages/VideoUploadImg.png")
        UploadBtn['image'] = VideoImg
        UploadBtn.image = VideoImg

    else:

        VideoMode = False
        VideoImg = PhotoImage(file=f"AppImages/UploadImg.png")
        UploadBtn['image'] = VideoImg
        UploadBtn.image = VideoImg

    # Resets the Output Window and Text Labels
    OutputWindowLabel.image = ""
    FileNameLabel.configure(text="File Name: No File Selected")
    FaceCountLabel.configure(text="Result: None")


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
    command=FilePrompt,
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
    command=FaceDetection,
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
