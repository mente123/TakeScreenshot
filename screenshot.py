import imp
import time
import pyautogui
import tkinter as tk # tkinter is used to work with widgets.

def screenShot():
    name = int(round(time.time()*1000))
    name = '/home/mente/Documents/Mente/Codes/pythonprojects/projectone/projectsenv/screenshots/{}.png'.format(name)  # we can create a folder to store the screenshots.
    time.sleep(5)
    img = pyautogui.screenshot('test.png') #giving a format to the picture that is going to be taken
    img.show()
    
    
root = tk.Tk()
frame = tk.Frame(root)    
frame.pack()

button = tk.Button(
    frame,
    text = "Take a screenshot",
    command= screenShot
)

button.pack(side=tk.LEFT)
 
close =  tk.Button(
    frame,
    text = "Close",
    command= quit
)

close.pack(side=tk.LEFT)

root.mainloop()
screenShot()

# The image will be saved in this project folder
# The image will be overritten so we have to create a variable with a random number to store the image
# There will be two buttons for the gui which says take a screenshot and quit
