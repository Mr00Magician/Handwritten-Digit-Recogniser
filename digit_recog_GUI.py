from tkinter import * 
from PIL import Image, ImageDraw
from tensorflow import keras as k
import numpy as n
import cv2
 
loaded_SNN = k.models.load_model('SequentialNN.h5')

def draw(event):
    x1 = event.x - 10
    y1 = event.y - 10
    x2 = event.x + 10
    y2 = event.y + 10
    can.create_rectangle(x1, y1, x2, y2, fill = 'black')
    img_draw.rectangle((x1, y1, x2, y2), fill = 'white')

def clear():
    global img, img_draw
    can.delete('all')
    img = Image.new('RGB', (500, 400), (0, 0, 0))
    img_draw = ImageDraw.Draw(img)

def predict():
    img_array = n.array(img)
    img_array = cv2.resize(img_array, (28, 28))
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_array = n.array(img_array, dtype = 'int32').reshape(1, 28, 28)

    pred = loaded_SNN.predict([img_array])
    final_pred = n.argmax(pred) 
    Label(main_frame, text = f'The prediction is : {final_pred}', font = 'comicsansms 15 bold', fg = 'blue').grid(row = 6, column = 1, columnspan = 2)

root = Tk()
root.title("Digit Recogniser")

swid = int(root.winfo_screenwidth()/1.5)
sht = int(root.winfo_screenheight()/1.5)

hswid = int(root.winfo_screenwidth()/2)
hsht = int(root.winfo_screenheight()/2)

root.geometry(f"{swid}x{sht}+{swid - hswid}+{sht - hsht - 20}")
root.minsize(swid, sht)


main_frame = Frame(root)
main_frame.pack()
Label(main_frame, text = 'Draw a digit below', font = 'comicsansms 20 bold', justify = CENTER).grid(row = 0, column = 0, columnspan = 4)
can = Canvas(main_frame, bg = 'white', width = 500, height = 400)
can.grid(row = 1, column = 0, rowspan = 4, columnspan = 4)

predict_button = Button(main_frame, text = 'Predict', bg = 'lightgreen', font = 'comicsansms 15 bold', width = 15, command = predict).grid(row = 5, column = 0, columnspan = 2)
clear_button = Button(main_frame, text = 'Clear', bg = 'lightgreen', font = 'comicsansms 15 bold', width = 15, command = clear).grid(row = 5, column = 2, columnspan = 2)

can.bind('<B1-Motion>', draw)

img = Image.new('RGB', (500, 400), (0, 0, 0))
img_draw = ImageDraw.Draw(img)

root.mainloop()