from tkinter import *
from PIL import Image, ImageTk

#screen
screen=Tk()
screen.title("Secret Note's")
screen.minsize(width=400,height=600)

#load the image
image_open = Image.open("/Users/eminsmacbookpro/PycharmProjects/SecretNotes/top_secret.jpg")
image_upload= ImageTk.PhotoImage(image_open)

#image resized for label
resized_image = image_open.resize((100, 100))
image_upload = ImageTk.PhotoImage(resized_image)

#label for image
image_label=Label(screen,image=image_upload,width=100,height=100)
image_label.place(relx=0.7,rely=0.8)

#label for note title
note_title_label=Label(text="Enter your note title:")
note_title_label = Label(text="Enter your note title:",font=("Arial", 14))
note_title_label.pack(pady=20)

#label for secret note
secret_note_label = Label(text="Enter your note title:",font=("Arial", 14))
secret_note_label.pack(pady=20)

#entry for note title
entry_note_title=Entry()
entry_note_title.place(relx=0.5,rely=0.09,anchor="center")

#text: multi lines
text_for_note=Text(width=40,height=20) #Uzun yazılar yazmak için kullanılır.
text_for_note.place(relx=0.5,rely=0.40,anchor="center")

#label for password
label_password=Label(text="Enter master key(password)",font=("Arial",14))
label_password.place(relx=0.5,rely=0.7,anchor="center")

#entry for password
entry_password=Entry()
entry_password.place(relx=0.5,rely=0.74,anchor="center")

#button for save & Encrypt
button_save_encrypt=Button(text="Save & Encrypt",font=("Arial",14))
button_save_encrypt.place(relx=0.5,rely=0.79,anchor="center",width=150)

#button for Decrypt
button_decrypt=Button(text="Decrypt",font=("Arial",14))
button_decrypt.place(relx=0.5,rely=0.84,anchor="center",width=75)

screen.mainloop()
