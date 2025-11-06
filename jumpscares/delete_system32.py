import tkinter as tk
from tkinter import ttk

default_font = ("Segoe UI", 9)

def window():
    confirmation_window = tk.Tk()
    confirmation_window.title("Delete Folder")
    confirmation_window.geometry("460x200")
    confirmation_window.resizable(False, False)
    confirmation_window.configure(bg="white")

    # main frame
    frame = ttk.Frame(confirmation_window, padding=(20, 20, 20, 20))
    frame.pack(fill="both", expand=True)

    # question
    confirm_text = "Are you sure you want to permanently delete this folder?"
    ttk.Label(
        frame, text=confirm_text, font=default_font, wraplength=400, justify="left"
    ).pack(anchor="w", pady=(0, 10))

    # file path
    ttk.Label(frame, text=r"C:\Windows\System32", font=default_font).pack(
        anchor="w", pady=(0, 3)
    )

    # date created
    ttk.Label(frame, text="Date created: 02.08.2023", font=default_font).pack(
        anchor="w", pady=(0, 20)
    )

    # button frame (bottom-right)
    button_frame = ttk.Frame(frame)
    button_frame.pack(anchor="e")

    def choose_yes():
        confirmation_window.destroy()

    def choose_no():
        confirmation_window.destroy()

    # buttons side by side
    yes_btn = ttk.Button(button_frame, text="Yes", width=10, command=choose_yes)
    no_btn = ttk.Button(button_frame, text="No", width=10, command=choose_no)

    yes_btn.pack(side="left", padx=(0, 8))
    no_btn.pack(side="left")

    yes_btn.focus_set()

    confirmation_window.mainloop()

window()
