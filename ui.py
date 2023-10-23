import tkinter as tk
from file import load_file, save_result
from processing import decrypt_text


def create_ui():
    # Crear la ventana principal
    window = tk.Tk()
    window.title("ATBASH")
    window.geometry("600x400")

    # Crear frames para la entrada y el resultado
    input_frame = tk.Frame(window, padx=10, pady=10)
    result_frame = tk.Frame(window, padx=10, pady=10)

    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    result_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # --- Configuración de widgets y botones para entrada y resultado ---

    # Crear widgets para la entrada
    input_label = tk.Label(input_frame, text="Descifrar texto:")
    input_text = tk.Text(input_frame, height=10, width=30)
    input_label_o = tk.Label(input_frame, text=" -o- ")
    load_button = tk.Button(input_frame, text="Cargar archivo", command=load_file)

    input_label.grid(row=0, column=0, columnspan=3)
    input_text.grid(row=1, column=0, columnspan=3)
    input_label_o.grid(row=2, column=0, columnspan=3)
    load_button.grid(row=3, column=0, columnspan=3)

    # Crear widgets para opciones de eliminación de caracteres no alfabéticos y conversión a mayúsculas
    remove_non_alpha = tk.IntVar()
    remove_checkbox = tk.Checkbutton(input_frame, text="Eliminar caracteres no alfabéticos", variable=remove_non_alpha)
    convert_to_upper = tk.IntVar()
    convert_checkbox = tk.Checkbutton(input_frame, text="Convertir a mayúsculas", variable=convert_to_upper)

    remove_checkbox.grid(row=4, column=0, sticky="w")
    convert_checkbox.grid(row=5, column=0, sticky="w")

    # Descifrar
    decrypt_button = tk.Button(input_frame, text="Descifrar", bg="#0074cc", fg="white", highlightbackground="#0074cc",
                               command=lambda: decrypt_text(input_text, result_text, remove_non_alpha, convert_to_upper))
    decrypt_button.grid(row=6, column=0, columnspan=3)

    # Crear widgets para el resultado
    result_label = tk.Label(result_frame, text="Resultado:")
    result_text = tk.Text(result_frame, height=10, width=30)

    input_label_o2 = tk.Label(result_frame, text=" -o- ")
    save_button = tk.Button(result_frame, text="Guardar resultado", command=save_result)

    result_label.grid(row=0, column=0, columnspan=2)
    result_text.grid(row=1, column=0, columnspan=2)
    input_label_o2.grid(row=2, column=0, columnspan=2)
    save_button.grid(row=3, column=0, columnspan=2)

    return window
