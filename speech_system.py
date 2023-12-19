import tkinter as tk
from PIL import Image, ImageTk

from tkinter import filedialog
from tkinter.ttk  import Combobox
import pyttsx3
import os

root = tk.Tk()
root.title('Text to Speech converter')
root .geometry('900x500')
root.resizable(False,False)
root.configure(bg='#305065')

label_result=tk.Label(root,width=700,height=2,text="Text To Speech",font=('arial',30),bg='white',anchor="w", justify="left",padx=100)
label_result.place(x=0,y=20)


# Speak
mike = Image.open('mike.png')  # Provide the correct path to 'mike.png'
width, height = 70, 70
mike_img = mike.resize((width, height))
mikeimg = ImageTk.PhotoImage(mike_img)

mike_label = tk.Label(root, image=mikeimg, bg="#0E0E0E", pady=100)
mike_label.place(x=20, y=40)

# Text area

text_area = tk.Text(root,font=('arial',30),bg='white',relief='groove',wrap='word')
text_area.place(x=10,y=130,width=470,height=330)

gender_combobox=Combobox(root,value=[ 'Male','Female'],font=('arial',15),state='r',width=12)
gender_combobox.place(x=520,y=200)
gender_combobox.set('Male')
gender_label= tk.Label(root,text='Voice',font=('arial',20),fg='white',bg="#305065")
gender_label.place(x=550,y=150)

speed_combobox=Combobox(root,value=[ 'Normal','Fast','Slow'],font=('arial',15),state='r',width=12)
speed_combobox.place(x=700,y=200)
speed_combobox.set('Normal')
speed_label= tk.Label(root,text='Speed',font=('arial',20),fg='white',bg="#305065")
speed_label.place(x=730,y=150)

btn= tk.Button(root,text='Speak',width=10,font=('arial',14,'bold'), justify="right",padx=10)
btn.place(x=520,y=280)

# Speak
Speak = Image.open('Speak.png')  # Provide the correct path to 'Speak.png'
width, height = 30, 30
Speak_img = Speak.resize((width, height))
Speakimg = ImageTk.PhotoImage(Speak_img)

Speak_label = tk.Label(root, image=Speakimg, bg="white", pady=100)
Speak_label.place(x=520, y=283)

# download
btn2= tk.Button(root,text='Download',width=10,font=('arial',14,'bold'), justify="right",padx=15)
btn2.place(x=700,y=280)
download = Image.open('download.png')  # Provide the correct path to 'download.png'
width, height = 30, 30
download_img = download.resize((width, height))
downloadimg = ImageTk.PhotoImage(download_img)

download_label = tk.Label(root, image=downloadimg, bg="white", pady=100)
download_label.place(x=700, y=283)


root.mainloop()