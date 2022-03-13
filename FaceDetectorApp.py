
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


# Starting the Tkinter MainLoop
FaceDetectionApp.mainloop()
