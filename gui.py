import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

#load the trained model to classify the images

from keras.models import load_model
model = load_model('model1_cifar_10epoch.h5')

#dictionary to label all the CIFAR-10 dataset classes.

classes = { 
    0:'aeroplane',
    1:'automobile',
    2:'bird',
    3:'cat',
    4:'deer',
    5:'dog',
    6:'frog',
    7:'horse',
    8:'ship',
    9:'truck' 
}
#initialise GUI

top=tk.Tk()
top.geometry('800x600')
top.title('Image Classification')
top.configure(background='#521027')
label=Label(top,background='#521027', font=('Comic Sans MS',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict([image])[0]
    # sign = classes[pred]
    # print(sign)
    if(pred[9]):
        label.configure(foreground='#011638', text='Truck')
        print(pred)
    elif(pred[8]): 
        label.configure(foreground='#011638', text='Kapal')
        print(pred)
    elif(pred[1]): 
        label.configure(foreground='#011638', text='Mobil')
        print(pred)
    else:
        label.configure(foreground='#011638', text='Gajelas blok')
        print(pred)
    # label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Foto",
   command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
font=('Comic Sans MS',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload foto",command=upload_image,
  padx=10,pady=5)

upload.configure(background='#364156', foreground='white',
    font=('Comic Sans MS',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Image Classification", pady=20, font=('Comic Sans MS',20,'bold'))

heading.configure(background='#521027',foreground='#364156')
heading.pack()
top.mainloop()