##Imports
from tkinter import * #Imports everything of the main module Tk
from tkinter import ttk #Import the submodule ttk

##Functions
def converter(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

##Root Window
root = Tk() #Create the root window object
root.title("Distance converter (feet to meters)") #Customize the window title

##Mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12") #Create a frame within root and set the padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #Set the coordinates for the frame
root.columnconfigure(0, weight=1) #Set the weight of the column 0 to 1
root.rowconfigure(0, weight=1) #Set the weight of the row 0 to 1

##Feet Entry
feet = StringVar() #Create the feet v   ariable
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) #Create an entry within mainframe, set the width and define the variable related to the entry (feet)
feet_entry.grid(column=2, row=1, sticky=(W, E)) #Set the coordinates for the entry

##Meters Label
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) #Set the coordinates and the variable related to the label (meters)

##Calculate Button
ttk.Button(mainframe, text="Calculate", command=converter).grid(column=3, row=3, sticky=W)

##Output Labels
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#Adding horizontal and vertical padding to the elements within mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus() #Focus on the feet_entry input
root.bind("<Return>", converter) #If press "enter", then the function "converter" is executed

root.mainloop() # Start the event loop