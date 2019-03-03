# -*- coding: utf-8 -*-
import tkinter
from tkinter import filedialog, Tk,StringVar,Button,Label,Text,Canvas,Entry
from PIL import  Image, ImageTk
#Tk.attributes("-fullscreen", True)
top = Tk()
top.attributes("-zoom", True)
top.title = 'Retail-Billing'
#top.geometry('1200x1200')
img_c_width = 400
img_c_height = 200
canvas = Canvas(top, width=img_c_width,height=500, bd=0,bg='white')

canvas.grid(row=1, column=0)



def showImg():
    File = filedialog.askopenfilename(title='Open Image')
    e.set(File)
    load = Image.open(e.get())
    w, h = load.size
    load = load.resize((img_c_width, img_c_height))
    imgfile = ImageTk.PhotoImage(load )
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)


e = StringVar()

submit_button = Button(top, bd=0,text ='Open', command = showImg)
submit_button.grid(row=0, column=0)

def plot_bill(t,data):

    medium_font = large_font = ('Verdana',14)
    large_font = ('Verdana', 14)
    ## plot headers
    headers = ["Name","Items","Unit Price","Total"]
    c = 0
    for header in headers:
        b = Entry(t, font=medium_font)
        b.insert(0, header)
        b.grid(row=0, column=c)
        c +=1



    rows = len(data)
    cols = 4

    total = 25.00
    for i in range(rows):
        for j in range(cols):
            b = Entry(t,text=data[i][j],font=medium_font)
            b.delete(0, tkinter.END)
            b.insert(0,str(data[i][j]))
            b.grid(row=i+1,column=j)
    #t.update()

    b = Entry(t,font=large_font)
    b.insert(0,total)
    b.grid(row=rows+1,column=cols-1)

    b = Entry(t,font=large_font)
    b.insert(0,"Total")
    b.grid(row=rows+1,column=0)


def Predict():
    textvar = "Total bill is {}".format(121.01)
    # t1.delete(0.0, tkinter.END)
    # t1.insert('insert', textvar+'\n')
    dummy_data = [["sample1",10,1,10],["sample2",2,1,2]]
    plot_bill(t2,dummy_data)
    #t1.update()
    
    
submit_button = Button(top, text ='Bill IT', command = Predict)
submit_button.grid(row=0, column=1)

l1=Label(top,text='Please <Open> a RGB image, then press <Predict> ')
l1.grid(row=2)



result=Canvas(top,bd=0, width=150,height=img_c_height)
result.grid(row=1, column=1)
# t1 = Text(result,bd=0,width=100,height=10,font='Fixdsys -14')
# t1.grid(row=0,column=0)
t2 = Text(result, bd=0, width=150, height=80, font='Fixdsys -14')
t2.grid(row=1, column=0)
top.mainloop()