import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_special_chars, use_numbers):
    characters = string.ascii_letters
    if use_special_chars:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    if not characters:
        messagebox.showerror("Error", "please add one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_from_gui():
    length = int(length_entry.get())
    special_chars = special_chars_var.get()
    numbers = numbers_var.get()

    password = generate_password(length, special_chars, numbers)

    if password:
        password_display.config(state=tk.NORMAL) 
        password_display.delete("1.0", tk.END)   
        password_display.insert(tk.END, password) 
        password_display.config(state=tk.DISABLED)

def copy_to_clipboard():
    password = password_display.get("1.0", tk.END).strip() 
    if password:
        root.clipboard_clear() 
        root.clipboard_append(password) 
        root.clipboard_update() 


root = tk.Tk()
root.title("Password Generator")
root.geometry("330x195+691+244")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_from_gui)
generate_button.pack()

password_display = tk.Text(root, height=1, width=30, state=tk.DISABLED)
password_display.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
