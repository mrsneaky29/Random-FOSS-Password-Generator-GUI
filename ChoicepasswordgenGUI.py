import tkinter
from tkinter import *


window = Tk()
window.title("FOSS Password Generator with GUI")
numberofalphabets = tkinter.Spinbox(window,from_=0,to_=100000000,width=5)
numberofdigits = tkinter.Spinbox(window,from_=0,to_=100000000,width=5)
numberofsymbols = tkinter.Spinbox(window,from_=0,to_=100000000,width=5)
window.mainloop()