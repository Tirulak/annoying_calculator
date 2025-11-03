import tkinter as tk
from tkinter import ttk

default_font = ("Segoe UI", 9)

def window():
    confirmation_window = tk.Tk()
    confirmation_window.title("Delete Folder")
    confirmation_window.geometry("460x200")
    confirmation_window.resizable(False, False)

    confirmation_window.attributes("-toolwindow", True)

    frame = ttk.Frame(confirmation_window, padding=(12, 12, 12, 12))
    frame.grid(row=0, column=0, sticky="nsew")

    confirm_deletion_question = "Are you sure you want to permanently delete this folder?"
    confirm_deletion_question_label = ttk.Label(frame, text=confirm_deletion_question, font=default_font, wraplength=360, justify="left")
    confirm_deletion_question_label.grid(row=0, column=1, sticky="w")

    info_about_file_path = "C:\Windows\System32"
    info_about_file_path_label = ttk.Label(frame, text=info_about_file_path, font=default_font, wraplength=360, justify="left")
    info_about_file_path_label.grid(row=0, column=0, sticky="w", pady=(8, 2))

    info_about_file_date = "Date created: 02.08.2023"
    info_about_file_date_label = ttk.Label(frame, text=info_about_file_date, font=default_font, wraplength=360, justify="left")
    info_about_file_date_label.grid(row=1, column=0, sticky="w")


    def choose_yes():
        pass
    def choose_no():
        pass

    button_frame = ttk.Frame(frame)
    button_frame.grid(row=2, column=0, columnspan=2, sticky="e")

    button_yes = ttk.Button(button_frame, text="Yes", width=9, command=lambda: choose_yes())
    button_no = ttk.Button(button_frame, text="No", width=9, command=lambda: choose_no())

    button_yes.grid(row=0, column=0, padx=(6, 0))
    button_no.grid(row=0, column=1, padx=(0, 6))

    button_yes.focus_set()

    confirmation_window.mainloop()

window()
