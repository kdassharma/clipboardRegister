import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import time
from ScrollableFrame import ScrollableFrame
import pyperclip

# pyperclip.copy('The text to be copied to the clipboard.')
# pyperclip.paste()

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 500
MAX_MEMORY = 10
CURRENT_FRAME = 1
CURRENT_CLIPBOARD_CONTENT = ''

root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
canvas.pack()

while True: 

    titleFrame = tk.Frame(root, bg = '#000000', highlightbackground="black", highlightthickness=0.5)
    titleFrame.place(relx=0,rely=0, relwidth=1, relheight = (1/(MAX_MEMORY+1)))

    backgroundImg = ImageTk.PhotoImage(Image.open("./assets/frame_background.jpg")) 
    # backroundLabel = tk.Label(titleFrame, image = backgroundImg)
    # backroundLabel.place(relwidth=1, relheight=1)

    TEMPORARY_CLIPBOARD_CONTENT = root.clipboard_get()

    if CURRENT_CLIPBOARD_CONTENT != TEMPORARY_CLIPBOARD_CONTENT:

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        tempFrame = tk.Frame(root, bg = '#f2f2f2', highlightbackground="black", highlightthickness=0.5)
        tempFrame.place(relx=0,rely=(1/(MAX_MEMORY+1)) * (CURRENT_FRAME), relwidth=1 ,relheight = (1/(MAX_MEMORY+1)))
  
        contentLabel = tk.Label(tempFrame, text=TEMPORARY_CLIPBOARD_CONTENT,font=('Courier',10))
        contentLabel.place(relwidth=1, relheight = 1)       

        timeLabel = tk.Label(tempFrame, text=current_time, font=('Courier',10))
        timeLabel.place(relx=0,rely=0, relwidth=0.1, relheight = 0.2)

        # copyButton = tk.Button(tempFrame, text ="Copy", command = copyText)
        copyButton = tk.Button(tempFrame, text ="Copy")
        copyButton.place(relx=1,rely=1, relwidth=0.2, relheight = 0.2)
        
        CURRENT_FRAME += 1

        CURRENT_CLIPBOARD_CONTENT = TEMPORARY_CLIPBOARD_CONTENT
       

    time.sleep(0.1)
    root.update_idletasks()
    root.update()

root.mainloop()

# old 
# new
# newer