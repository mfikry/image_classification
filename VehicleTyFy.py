#Import Library Pembuatan Aplikasi GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import *

#Library untuk citra
from PIL import ImageTk, Image

#Library untuk array
import numpy

#Untuk load model
from keras.models import load_model
model = load_model('model_klasifikasi_alat_transportasi.h5')

#Library untuk qrcode
from datetime import date,datetime
import pyqrcode

#Inisialisasi GUI
root=tk.Tk()
root.geometry('800x550') #Ukuran window
root.title('Klasifikasi Citra Alat Transportasi')
label=Label(root,font=('Arial',20))
sign_image = Label(root)
heading = Label(root, text="VehicleTyFy", font=('Arial',20,'bold'))
heading.place(x=100,y=110)
catatan = Label(root, text="QR code akan otomatis tersimpan di Folder Alat Transportasi!", font=('Arial',10,'italic'))
catatan.place(x=200,y=530)
#Membuat function klasifikasi
def klasifikasi(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict([image])[0]
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H.%M.%S")
    Jam = now.strftime("%H:%M:%S")
    d1 = today.strftime("%d-%m-%Y") 
    if(pred[9]):
        label.configure(text='Truck',  font=('Arial',14,'bold'))
        teks_qr=("Aset Alat Transportasi adalah Truck"+'\nPada Tanggal: '+d1+'\nJam: '+Jam)
         #QR-Code
        im = pyqrcode.QRCode(teks_qr)
        im.png('test.png',scale=10)
        im = Image.open('test.png') 
        im = im.convert("RGB")
        logo = Image.open(file_path)
        box = (220,220,340,340)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.save('Alat Transportasi/Truck/Hasil_QrCode_' + current_time + '.jpg')
    elif(pred[8]): 
        label.configure(text='Kapal Layar',  font=('Arial',14,'bold'))
        teks_qr=("Aset Alat Transportasi adalah Kapal"+'\nPada Tanggal: '+d1+'\nJam: '+Jam)
        #QR-Code
        im = pyqrcode.QRCode(teks_qr)
        im.png('test.png',scale=10)
        im = Image.open('test.png') 
        im = im.convert("RGB")
        logo = Image.open(file_path)
        box = (220,220,340,340)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.save('Alat Transportasi/Kapal/Hasil_QrCode_' + current_time + '.jpg')
        label.place(x=550,y=410)
    elif(pred[1]): 
        label.configure(text='Mobil',  font=('Arial',14,'bold'))
        teks_qr=("Aset Alat Transportasi adalah Mobil"+'\nPada Tanggal: '+d1+'\nJam: '+Jam)
        #QR-Code
        im = pyqrcode.QRCode(teks_qr)
        im.png('test.png',scale=10)
        im = Image.open('test.png') 
        im = im.convert("RGB")
        logo = Image.open(file_path)
        box = (220,220,340,340)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.save('Alat Transportasi/Mobil/Hasil_QrCode_' + current_time + '.jpg')
    else:
        label.configure(text='Tidak Diketahui',  font=('Arial',14,'bold'))
        label.place(x=540,y=410)

#Membuat button prediksi
def tampilkan_klasifikasi_button(file_path):
    klasifikasi_b=Button(root,text="Prediksi", font=('Arial',13),command=lambda: klasifikasi(file_path),padx=10,pady=10)
    klasifikasi_b.place(x=200,y=250)

#Membuat function upload foto    
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((root.winfo_width()/2.25),(root.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        tampilkan_klasifikasi_button(file_path)
    except:
        pass

#button upload
upload=Button(root,text="Upload Foto",font=('Arial',13),command=upload_image,padx=10,pady=10)
upload.place(x=50,y=250)

#posisi image yang diupload
sign_image.place(x=450,y=30,width=300,height=300)

#posisi label prediksi
label.place(x=590,y=410)

#hasil prediksi txt
hasil_txt = tk.Label(root, text="Hasil Prediksi :" , font=('Arial',14))
hasil_txt.place(x=500,y=310,width=230,height=60)

root.mainloop()