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

# Create the main window
root = tk.Tk()
root.title("Dictionary App")

# Create and pack widgets
label = tk.Label(root, text="Enter a word:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

search_button = tk.Button(root, text="Search", command=get_definition)
search_button.pack()

definition_text = tk.Label(root, text="", justify="left")
definition_text.pack()

# Start the main loop
root.mainloop()
