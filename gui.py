from Tkinter import *
import report
import cv2
import numpy as np

def makereport():
   report.rept(str(e1.get()))
   e1.delete(0,END)

def closeall():
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   

master = Tk()
Label(master, text="Enter Image Path:").grid(row=0)


e1 = Entry(master)



e1.grid(row=0, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='End', command=closeall).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Show', command=makereport).grid(row=3, column=2, sticky=W, pady=4)


mainloop( )