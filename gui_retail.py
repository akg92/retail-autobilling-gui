# -*- coding: utf-8 -*-
import tkinter
from tkinter import filedialog, Tk,StringVar,Button,Label,Text,Canvas,Entry
from PIL import  Image, ImageTk
import  numpy as np
import sys



#Tk.attributes("-fullscreen", True)
top = Tk()
top.attributes("-zoom", True)
top.title = 'Retail-Billing'
#top.geometry('1200x1200')
img_c_width = 400
img_c_height = 500
canvas = Canvas(top, width=img_c_width,height=500, bd=0,bg='white')
canvas.grid(row=1, column=0)

## extra code for testing multiple models.
model_type = "multi"
if len(sys.argv)==2:
    model_type = sys.argv[1]






# import keras
# import keras

sys.path.append('../retail-product-auto-billing/retinanet')
sys.path.append('../retail-product-auto-billing/retinanet/keras_retinanet')
# import keras_retinanet
# from keras_retinanet import models
# from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
# from keras_retinanet.utils.visualization import draw_box, draw_caption
# from keras_retinanet.utils.colors import label_color
from prediction_factory import  Single,Multi

import json
import os

MODEL_DIR = './images'
IMG_FILE = ''
PREDICTION_CONFIDENCE = 0.65

categories = None

# ## load categories
# with open('annotation.json') as f:
#     json_obj = json.load(f)
#     categories = json_obj['categories']


def get_precition_map(labels):
    result = []
    label_set = set(labels)
    for label in label_set:
        name = categories[label]['name']
        count = labels.count(label)
        price = int(label/10)
        result.append([name,count,price,price*count])
    return  result



def predict_labels():
    global  model
    img_path = e.get()
    image = read_image_bgr(img_path)
    image = preprocess_image(image)
    image, scale = resize_image(image)
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    result = []
    result_score = []
    for box,score,label in zip(boxes[0],scores[0],labels[0]):
        if score<PREDICTION_CONFIDENCE:
            break
        else:
            result.append(label)
            result_score.append(score)
    return result,result_score

def showImg():
    File = filedialog.askopenfilename(title='Open Image')
    e.set(File)
    #file_name = e.get()
    load = Image.open(e.get())
    w, h = load.size
    load = load.resize((img_c_width, img_c_height))
    imgfile = ImageTk.PhotoImage(load)
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)


e = StringVar()

submit_button = Button(top, bd=0,text ='Open', command = showImg)
submit_button.grid(row=0, column=0)

old_rows = -1
def plot_bill(t,data):

    global  old_rows
    medium_font = large_font = ('Verdana',14)
    large_font = ('Verdana', 14)
    ## plot headers
    headers = ["Name","Items","Unit Price","Total"]
    c = 0
    for child in t.winfo_children():
        child.destroy()
    old_rows = len(data)
    for header in headers:
        b = Entry(t, font=medium_font,bd=0)
        b.insert(0, header)
        b.grid(row=0, column=c)
        c +=1



    rows = len(data)
    cols = 4

    total = 0

    ## clear all the old values



    for i in range(rows):
        for j in range(cols):
            b = Entry(t,bd=0,font=medium_font)
            b.delete(0, tkinter.END)
            b.insert(0,str(data[i][j]))
            b.grid(row=i+1,column=j)
        total += data[i][3]
    #t.update()

    b = Entry(t,font=large_font)
    b.insert(0,total)
    b.grid(row=rows+1,column=cols-1)

    b = Entry(t,font=large_font)
    b.insert(0,"Total")
    b.grid(row=rows+1,column=0)


def Predict():
    img_path = e.get()
    textvar = "Total bill is {}".format(121.01)
    if model_type=='single':
        model = Single()
    else:
        model = Multi()

    data = model.predict(img_path)

    print(data)
    plot_bill(t2, data)


def Predict_old():
    textvar = "Total bill is {}".format(121.01)
    labels,scores = predict_labels()
    #print(labels)
    #print(scores)
    data = get_precition_map(labels)
    print(data)
    plot_bill(t2, data)
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