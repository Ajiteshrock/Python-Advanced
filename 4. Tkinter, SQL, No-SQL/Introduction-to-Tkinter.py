#import important/required lib
import tkinter
from tkinter import *

mainWindow = tkinter.Tk() #initializing the main window
mainWindow.title("Example Tkinter") #setting the title

headingLabel = tkinter.Label(mainWindow, text="Hello World") #heading of the window
headingLabel.pack() # packing this window

userEntry = Entry(mainWindow) #an entry block
userEntry.pack()

def fun(): #creating funcion for showing the name you entered AJ
    name = userEntry.get()
    print("Hello your name is: ",name)

showButton = tkinter.Button(mainWindow,text="Button",command=lambda:fun())
showButton.pack()

mainWindow.mainloop() #this is really important 


## Simple Calculator


