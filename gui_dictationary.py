import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

def get_definition():
    word = entry.get()
    dictionary = PyDictionary()

    try:
        definitions = dictionary.meaning(word)
        if not definitions:
            messagebox.showinfo("Definition", f"No definitions found for '{word}'")
        else:
            definition_text.config(text="\n".join([f"{pos}: {', '.join(definitions[pos])}" for pos in definitions]))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear_entries():
    entry.delete(0, tk.END)
    definition_text.config(text="")
    
# Create the main window
root = tk.Tk()
root.title("Dictionary App")

# Create and pack widgets
label = tk.Label(root, text="Enter a word:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=get_definition)
search_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries, font=("Arial", 12))
clear_button.pack(pady=10)

definition_text = tk.Label(root, text="", justify="left")
definition_text.pack(pady=10)

# Start the main loop
root.mainloop()
