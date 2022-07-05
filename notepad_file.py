#Import os library
import os
#import everything from tkinter
from tkinter import *
#To get the space above the message
from tkinter.messagebox import *
#To get the dialog box to open when required
from tkinter.filedialog import *

class Notepad:
   # Set up the root widget
   root = Tk()
   TextArea = Text(root)
   MenuBar = Menu(root)

   # To add scrollbar
   ScrollBar = Scrollbar(TextArea)
   __file = None

   def __init__(self,width,height):
   # Set window size as mentioned above (the default is 300x300)
      self.Width = width
      self.Height = height
     
      # the window text
      self.root.title("Untitled-Notepad")
      
      # Center the window
      screenWidth = self.root.winfo_screenwidth()
      screenHeight = self.root.winfo_screenheight()
      
      # For left-align
      left = (screenWidth / 2) - (self.Width / 2)
     
      # For right-align
      top = (screenHeight / 2) - (self.Height /2)
      
      # For top and bottom
      self.root.geometry('%dx%d+%d+%d' % (self.Width, self.Height, left, top))
      
      # To make the textarea auto resizable
      self.root.grid_rowconfigure(0, weight=1)
      self.root.grid_columnconfigure(0, weight=1)
      
      # Add controls (widget)
      self.TextArea.grid(sticky = N + E + S + W)
      
   def run(self):
        # Run main application
        self.root.mainloop()
 
# Run main application
object_notepad = Notepad(600,400)
object_notepad.run()
