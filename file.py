import tkinter as tk
from tkinter import filedialog


def load_file(input_text):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, text)


def save_result(result_text):
    result_text_data = result_text.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result_text_data)

