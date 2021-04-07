from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image

Canvas=Tk() 
Canvas.title("Image Converter")

label0=Label(Canvas,text="Image Converter",fg="white",bg="coral",font="time 40",width=14 ,borderwidth=5, relief="ridge")
label0.grid(row=1,column=0,columnspan=2,pady=5)

def jpgtopdf():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("Output-pdf.pdf", resolution=100.0)
    else:
        Label2=Label(Canvas,text="Error!!", width=20,bg="red",fg="white", font=("bold",20))
        Label2.grid(row=2, column=0,pady=10)

def jpgtopng():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("Output-png.png")
    else:
        Label2=Label(Canvas,text="Error!", width=20,bg="red",fg="white", font=("bold",20))
        Label2.grid(row=2, column=0,pady=10)


Label1=Label(Canvas,text="Choose a File", width=20, font=("bold",30),fg="#900d09")
Label1.grid(row=3, column=0)

btn1=Button(Canvas,text="JPG to PNG", width=20, height=1, bg="#9a7b48",fg="white",font=("poppins 25"),activebackground="coral",borderwidth=5, relief="raised",command=jpgtopng)
btn1.grid(row=5, column=0, columnspan=2,pady=10)
btn2=Button(Canvas,text="JPG to PDF", width=20, height=1, bg="#9a7b48",fg="white",font=("poppins 25"), activebackground="coral",borderwidth=5, relief="raised",command=jpgtopdf)
btn2.grid(row=7, column=0, columnspan=2,pady=10)

Canvas.mainloop()