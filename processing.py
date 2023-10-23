import tkinter as tk
from atbash import atbash_decrypt


def remove_non_alphabetic_chars(input_text, remove_non_alpha):
    input_text_data = input_text.get("1.0", "end-1c")
    if remove_non_alpha.get():
        input_text_data = ''.join(filter(str.isalpha, input_text_data))
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, input_text_data)


def convert_to_uppercase(input_text, convert_to_upper):
    input_text_data = input_text.get("1.0", "end-1c")
    if convert_to_upper.get():
        input_text_data = input_text_data.upper()
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, input_text_data)


def decrypt_text(input_text, result_text, remove_non_alpha, convert_to_upper):
    remove_non_alphabetic_chars(input_text, remove_non_alpha)
    convert_to_uppercase(input_text,  convert_to_upper)
    input_text_data = input_text.get("1.0", "end-1c")
    decrypted_text = atbash_decrypt(input_text_data)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, decrypted_text)
