# hazard5
import tkinter as tk
from tkinter import ttk, messagebox
import re

def validate_and_save():
    # Pobranie wartości z pól
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    education = education_var.get()
    gender = gender_var.get()

    # Walidacja nazwiska
    if not name:
        messagebox.showerror("Błąd", "Pole 'Imię i nazwisko' jest wymagane.")
        return
    if name.split()[-1][0].islower():
        messagebox.showerror("Błąd", "Nazwisko musi zaczynać się z wielkiej litery.")
        return

    # Walidacja adresu e-mail
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    if not re.match(email_pattern, email):
        email_entry.config(fg="blue")
        messagebox.showerror("Błąd", "Nieprawidłowy adres e-mail.")
        return
    else:
        email_entry.config(fg="black")

    # Walidacja edukacji i płci
    if not education:
        messagebox.showerror("Błąd", "Musisz wybrać poziom wykształcenia.")
        return
    if not gender:
        messagebox.showerror("Błąd", "Musisz wybrać płeć.")
        return

    # Wyświetlenie podsumowania
    messagebox.showinfo("Dane zapisane", f"Imię i nazwisko: {name}\nAdres email: {email}\nWykształcenie: {education}\nPłeć: {gender}")

# Główne okno
root = tk.Tk()
root.title("Ankieta zadowolenia klienta")

# Etykieta i pole edycyjne - Imię i nazwisko
name_label = tk.Label(root, text="Imię i nazwisko:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Etykieta i pole edycyjne - Adres email
email_label = tk.Label(root, text="Adres email:")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Lista rozwijalna - Wykształcenie
education_label = tk.Label(root, text="Wykształcenie:")
education_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
education_var = tk.StringVar()
education_combobox = ttk.Combobox(root, textvariable=education_var, state="readonly")
education_combobox['values'] = ("Podstawowe", "Średnie", "Wyższe", "Inne")
education_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Przyciski radiowe - Płeć
gender_label = tk.Label(root, text="Płeć:")
gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_frame = tk.Frame(root)
gender_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Radiobutton(gender_frame, text="Kobieta", variable=gender_var, value="Kobieta").pack(side="left")
tk.Radiobutton(gender_frame, text="Mężczyzna", variable=gender_var, value="Mężczyzna").pack(side="left")
tk.Radiobutton(gender_frame, text="Inna", variable=gender_var, value="Inna").pack(side="left")

# Przycisk Zapisz
save_button = tk.Button(root, text="Zapisz", bg="blue", fg="white", command=validate_and_save)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

# Konfiguracja siatki
root.columnconfigure(1, weight=1)

root.mainloop()
