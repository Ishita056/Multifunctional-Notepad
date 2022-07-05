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
   FileMenu = Menu(MenuBar, tearoff=0)

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
    # To open new file
      self.FileMenu.add_command(label="New",
   command=self.__newFile)
      
      # To open a already existing file
      self.FileMenu.add_command(label="Open",
   command=self.__openFile)
      
      # To save current file
      self.FileMenu.add_command(label="Save",
   command=self.__saveFile)
      
      # To create a line in the dialog
      self.FileMenu.add_separator()
      self.FileMenu.add_command(label="Exit",
   command=self.__quitApplication)
      self.MenuBar.add_cascade(label="File", menu=self.FileMenu)

      self.root.config(menu=self.MenuBar)
      self.ScrollBar.pack(side=RIGHT,fill=Y)
      
      # Scrollbar will adjust automatically according to the content
      self.ScrollBar.config(command=self.TextArea.yview)
      self.TextArea.config(yscrollcommand=self.ScrollBar.set)
   def __quitApplication(self):
      self.root.destroy()
    
   def __openFile(self):
      self.__file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
      if self.__file == "":
         # no file to open
         self.__file = None
      else:
         # Try to open the file
         # set the window title
         self.root.title(os.path.basename(self.__file) + " - Notepad")
         self.TextArea.delete(1.0,END)
         file = open(self.__file,"r")
         self.TextArea.insert(1.0,file.read())
         file.close()
   def __newFile(self):
      self.root.title("Untitled Notepad")
      self.__file = None
      self.TextArea.delete(1.0,END)
   def __saveFile(self):
      if self.__file == None:
         # Save as new file
         self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
      if self.__file == "":
         self.__file = None
      else:
         # Try to save the file
         file = open(self.__file,"w")
         file.write(self.TextArea.get(1.0,END))
         file.close()
         # Change the window title
         self.root.title(os.path.basename(self.__file) + " - Notepad") 
      
   def run(self):
        # Run main application
        self.root.mainloop()
 
# Run main application
object_notepad = Notepad(600,400)
object_notepad.run()
