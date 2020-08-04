import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import time
from ScrollableFrame import ScrollableFrame
import pyperclip

# Default application dimensions
CANVAS_HEIGHT = 700
CANVAS_WIDTH = 500

# Refresh Rate (times/sec)
REFRESH_RATE = 10

# The number of copies each canvas
MAX_MEMORY = 5

# Specifying which frame is currently at
CURRENT_FRAME = 0

# Keeping track of the clipboard content
CURRENT_CLIPBOARD_CONTENT = ''
labelArray = []

root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
canvas.pack()

while True: 

    TEMPORARY_CLIPBOARD_CONTENT = root.clipboard_get()

    # If something new is detected in the clipboard
    if CURRENT_CLIPBOARD_CONTENT != TEMPORARY_CLIPBOARD_CONTENT:
        
        # If the number of clips hits the total number permissible, then it clears the top frame
        if CURRENT_FRAME == MAX_MEMORY:
            canvas.delete("all")
            CURRENT_FRAME = 0

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        # Creating the frame for the clipboard content
        tempFrame = tk.Frame(root, bg = '#f2f2f2', highlightbackground="black", highlightthickness=0.5)
        tempFrame.place(relx=0,rely=(1/(MAX_MEMORY)) * (CURRENT_FRAME), relwidth=1 ,relheight = (1/(MAX_MEMORY)))
  
        # Creating the label for the message itself
        contentLabel = tk.Label(tempFrame, text=TEMPORARY_CLIPBOARD_CONTENT,font=('Courier',10))
        contentLabel.place(relwidth=1, relheight = 1)       

        # Creating the label for the time
        timeLabel = tk.Label(tempFrame, text=current_time, font=('Courier',10))
        timeLabel.place(relx=0,rely=0, relwidth=0.1, relheight = 0.2)

        # Remains to be implemented
        # copyButton = tk.Button(tempFrame, text ="Copy")
        # copyButton.place(relx=1,rely=1, relwidth=0.2, relheight = 0.2)
        
        CURRENT_FRAME += 1

        CURRENT_CLIPBOARD_CONTENT = TEMPORARY_CLIPBOARD_CONTENT
       
    time.sleep(1/REFRESH_RATE)
    root.update_idletasks()
    root.update()

root.mainloop()
