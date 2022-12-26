# import imp
import time
import pyautogui
import tkinter as tk # tkinter is used to work with widgets.
import os

#Let's get the username of the PC 
pcUser = os.environ.get("USERNAME") 

#This is where the screenshot will be placed
path = "C:/Users/" + pcUser + "/Pictures/Screenshots/"

#If the above directory doesn't exist we have to create it by:
if not (os.path.exists(path)):
    os.mkdir(path)

def screenShot():
    name = int(round(time.time()*1000))
    img = pyautogui.screenshot(path + "test.png") #giving a format to the picture that is going to be taken
    img.show()
    
    
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
