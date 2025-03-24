##Imports
from tkinter import *
from tkinter import ttk

##Root window
root = Tk()

##Frames
warningFrame = ttk.Frame(root).grid(column=0, row=0)
dangerFrame = ttk.Frame(root).grid(column=0, row=1)
successFrame = ttk.Frame(root).grid(column=0, row=2)

##Changing styles
s = ttk.Style()
s.configure("Warning.TFrame", background="yellow")
ttk.Frame(warningFrame, width="150", height="30", style="Warning.TFrame").grid(column=0, row=0)
s.configure("Danger.TFrame", background="red")
ttk.Frame(dangerFrame, width="150", height="30", style="Danger.TFrame").grid(column=0, row=1)
s.configure("Success.TFrame", background="green")
ttk.Frame(successFrame, width="150", height="30", style="Success.TFrame").grid(column=0, row=2)

##Labels

warningLabel = ttk.Label(warningFrame, text="This is a warning!", background="#FFFFB3").grid(column=0, row=0)
dangerLabel = ttk.Label(dangerFrame, text="This is danger label!", background="#FFB3B3").grid(column=0, row=1)
successLabel = ttk.Label(successFrame, text="This is a success label!", background="#D9FFB3").grid(column=0, row=2)

##Mainloop
root.mainloop()