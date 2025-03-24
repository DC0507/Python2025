##Imports
from tkinter import *
from tkinter import ttk

##Root Window
root = Tk()

##Mainframe
mainframe = ttk.Frame(root, padding=30)
mainframe.grid(column=0, row=0)

##Label
label1 = ttk.Label(mainframe, text="Just a simple label...")
label1.grid(column=0, row=0)

##Binding Events
label1.bind("<Enter>", lambda e:label1.configure(text="Moved mouse inside"))
label1.bind("<Leave>", lambda e:label1.configure(text="Moved mouse outside"))
label1.bind("<ButtonPress-1>", lambda e:label1.configure(text="Clicked left mouse button"))
label1.bind("<3>", lambda e:label1.configure(text="Clicked right mouse button"))
label1.bind("<Double-1>", lambda e:label1.configure(text="Double-clicked"))
label1.bind("<B3-Motion>", lambda e:label1.configure(text="Right button drag to %d,%d" % (e.x, e.y)))


##Mainloop
root.mainloop()