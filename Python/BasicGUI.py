'''
Created on Jun 5, 2017

@author: abhinav.jhanwar
'''

#1
'''import tkinter
top = tkinter.Tk()
top.mainloop()'''

#2 button
'''from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x250")         #TO SET UI DIMENSIONS

def helloCallBack():
    msg = messagebox.showinfo( "Hello Python", "Hello World")
    print(msg)

B = Button(top, text = "Hello", command = helloCallBack, width = 10)
B.place(x = 50,y = 50)
top.mainloop()'''

#3 canvas
from tkinter import *
from tkinter import messagebox

top = Tk()
C = Canvas(top, bg = "white", height = 250, width = 500)
coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')
oval = C.create_polygon(10,10, 70,10, 85,25, 70,40, 10,40,  fill = "black")
oval = C.create_polygon(105,10, 165,10, 180,25, 165,40, 105,40,  fill = "grey")
oval = C.create_polygon(200,10, 260,10, 275,25, 260,40, 200,40,  fill = "grey")
oval = C.create_polygon(295,10, 355,10, 370,25, 355,40, 295,40,  fill = "grey")
C.create_text(190,25,fill="white",font="timesnewroman 8",
                        text="1.Load               2.View               3.Train             4.Predict")
C.pack()
top.mainloop()