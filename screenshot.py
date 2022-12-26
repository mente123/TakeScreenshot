# import imp
import time
import pyautogui
import tkinter as tk # tkinter is used to work with widgets.
from tkinter.filedialog import asksaveasfilename
import os

def screenShot():
    extentions = [("Image Files", "*.png *.jpg")] #Default file extention of the screenshot
    img = pyautogui.screenshot() 
    file_name = asksaveasfilename(filetypes=extentions, defaultextension=extentions) #let the users save at their prefered locations
    if file_name:
        img.save(file_name)
    
    
    
root = tk.Tk()
frame = tk.Frame(root)    
frame.pack()

button = tk.Button(
    frame,
    text = "Take a screenshot",
    command= screenShot,
)

button.pack(side=tk.LEFT, ipady=20, ipadx=10)
 
close =  tk.Button(
    frame,
    text = "Close",
    command= quit,
   
)

close.pack(side=tk.LEFT, ipady=20, ipadx=10)

root.mainloop()
screenShot()

# The image will be saved in this project folder
# The image will be overritten so we have to create a variable with a random number to store the image
# There will be two buttons for the gui which says take a screenshot and quit
