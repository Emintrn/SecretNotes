from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64

# Screen
screen = Tk()
screen.title("Secret Note's")
screen.minsize(width=400, height=600)

# Encryption
#encode():string → byte,encode():string → byte,chr(65)-> 'A',ord('A')->65
#% 256 →(ASCII/Unicode translation
def encrypt(text, key):
    encrypted = ""
    for char in text:
        encrypted += chr((ord(char) + key) % 256)
    return base64.b64encode(encrypted.encode()).decode()

def decrypt(encoded_text, key):
    try:
        decoded = base64.b64decode(encoded_text).decode()
    except:
        return "❌Invalid encryption or password!"

    decrypted = ""
    for char in decoded:
        decrypted += chr((ord(char) - key) % 256)
    return decrypted

#Save/Encrypt Function
def note_title_function():
    title = entry_note_title.get()
    note = text_for_note.get("1.0", END).strip()
    password = entry_password.get()

    if title == "" or note == "" or password == "":
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    key = sum(ord(char) for char in password)
    encrypted_note = encrypt(note, key)

    try:
        with open("SecretNotes.txt", "a") as file:
            file.write(f"Title: {title}\n{encrypted_note}\n---\n")
        text_for_note.delete("1.0", END)
        messagebox.showinfo("Saved", "Note encrypted and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save note: {e}")

#Decrypt Function
def decrypt_note():
    title = entry_note_title.get()
    password = entry_password.get()

    if title == "" or password == "":
        messagebox.showwarning("Warning", "Please enter both title and password.")
        return

    try:
        with open("SecretNotes.txt", "r") as file:
            contents = file.read().split("---\n")

        found = False
        for block in contents:
            if block.strip().startswith(f"Title: {title}"):
                lines = block.strip().split("\n")
                encrypted_note = "".join(lines[1:])
                key = sum(ord(char) for char in password)
                decrypted_note = decrypt(encrypted_note, key)
                text_for_note.delete("1.0", END)
                text_for_note.insert(END, decrypted_note)
                found = True
                break

        if not found:
            messagebox.showerror("Error", "Note not found.")
        elif decrypted_note.startswith("❌"):
            messagebox.showerror("Error", "Wrong password or corrupt note.")
        else:
            messagebox.showinfo("Success", "Note decrypted!")

    except FileNotFoundError:
        messagebox.showerror("Error", "SecretNotes.txt not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Load and resize image
image_open = Image.open("/Users/eminsmacbookpro/PycharmProjects/SecretNotes/top_secret.jpg")
resized_image = image_open.resize((100, 100))
image_upload = ImageTk.PhotoImage(resized_image)

# Label for image
image_label = Label(screen, image=image_upload)
image_label.image = image_upload  # Referans koru
image_label.place(relx=0.7, rely=0.8)

# Label for note title
note_title_label = Label(text="Enter your note title:", font=("Arial", 14))
note_title_label.pack(pady=20)

# Label for secret note
secret_note_label = Label(text="Enter your secret note:", font=("Arial", 14))
secret_note_label.pack(pady=20)

# Entry for note title
entry_note_title = Entry()
entry_note_title.place(relx=0.5, rely=0.09, anchor="center")

# Text for secret note
text_for_note = Text(width=40, height=20)
text_for_note.place(relx=0.5, rely=0.40, anchor="center")

# Label for password
label_password = Label(text="Enter master key (password)", font=("Arial", 14))
label_password.place(relx=0.5, rely=0.7, anchor="center")

# Entry for password
entry_password = Entry()
entry_password.place(relx=0.5, rely=0.74, anchor="center")

# Button for Save & Encrypt
button_save_encrypt = Button(text="Save & Encrypt", font=("Arial", 14), command=note_title_function)
button_save_encrypt.place(relx=0.5, rely=0.79, anchor="center", width=150)

# Button for Decrypt
button_decrypt = Button(text="Decrypt", font=("Arial", 14), command=decrypt_note)
button_decrypt.place(relx=0.5, rely=0.84, anchor="center", width=75)

# Run
screen.mainloop()

