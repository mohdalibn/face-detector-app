
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


# Starting the Tkinter MainLoop
FaceDetectionApp.mainloop()
