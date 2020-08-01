import tkinter as tk
from PIL import ImageTk, Image
import time

# import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')
# pyperclip.paste()

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
MAX_MEMORY = 3
CURRENT_FRAME = 1
CURRENT_CLIPBOARD_CONTENT = ''

def checkClipboard():

    TEMPORARY_CLIPBOARD_CONTENT = root.clipboard_get()

    if CURRENT_CLIPBOARD_CONTENT != TEMPORARY_CLIPBOARD_CONTENT:
        createFrame(TEMPORARY_CLIPBOARD_CONTENT)
        CURRENT_CLIPBOARD_CONTENT = TEMPORARY_CLIPBOARD_CONTENT

def createFrame(content):

    global CURRENT_FRAME

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    
    tempFrame = tk.Frame(root, bg = '#f2f2f2', highlightbackground="black", highlightthickness=0.5)
    tempFrame.place(relx=0,rely=(1/(MAX_MEMORY+1)) * (CURRENT_FRAME), relwidth=1 ,relheight = (1/(MAX_MEMORY+1)))
    
    message = "{}: {}".format(current_time, content)
    label = tk.Label(tempFrame, textvariable=message)
    label.place(relx=0.5,rely=0.5,relwidth=1, relheight = 1, anchor = 'n')
    
    CURRENT_FRAME += 1

root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
canvas.pack()

titleFrame = tk.Frame(root, bg = '#000000', highlightbackground="black", highlightthickness=0.5)
titleFrame.place(relx=0,rely=0, relwidth=1, relheight = (1/(MAX_MEMORY+1)))

backgroundImg = ImageTk.PhotoImage(Image.open("./assets/frame_background.jpg")) 
backroundLabel = tk.Label(titleFrame, image = backgroundImg)
backroundLabel.place(relwidth=1, relheight=1)

# lambda: checkClipboard()
print(root.clipboard_get())

root.mainloop()
    
