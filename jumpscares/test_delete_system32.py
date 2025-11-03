import tkinter as tk
from tkinter import ttk

DEFAULT_FONT = ("Segoe UI", 9)
TITLE_FONT = ("Segoe UI", 10, "bold")

def draw_recycle_and_folder(canvas):
    """Draw a small recycle-bin icon near the top and a larger folder icon below."""
    # small recycle bin (top-left)
    # bin body
    canvas.create_rectangle(6, 6, 26, 28, outline="#7a7a7a", fill="#f6f6f6")
    # bin lid
    canvas.create_rectangle(2, 2, 30, 8, outline="#7a7a7a", fill="#e9e9e9")
    # recycle symbol (simple)
    canvas.create_oval(8, 10, 12, 14, outline="#5a8bd6", width=1)
    canvas.create_line(11, 11, 14, 11, arrow=tk.LAST, fill="#5a8bd6")

    # larger folder icon (lower-left)
    base_x = 6
    base_y = 48
    scale = 1.6
    # body
    canvas.create_rectangle(base_x + 6*scale, base_y + 10*scale,
                            base_x + 56*scale, base_y + 38*scale,
                            outline="#7a5a14", fill="#f0c75a")
    # tab
    canvas.create_rectangle(base_x + 6*scale, base_y + 4*scale,
                            base_x + 30*scale, base_y + 18*scale,
                            outline="#7a5a14", fill="#ffd773")
    # inner shadow line
    canvas.create_line(base_x + 8*scale, base_y + 20*scale,
                       base_x + 56*scale, base_y + 20*scale,
                       fill="#e2b34a")

def ask_prank_confirm(folder_path=r"C:\Windows\System32", folder_name="New folder", date_created="07-03-2018 19:35"):
    root = tk.Tk()
    root.title("Delete Folder")
    # keep a compact dialog size similar to the screenshot
    root.geometry("540x210")
    root.resizable(False, False)

    # try to reduce decorations (not all platforms support)
    try:
        root.attributes("-toolwindow", True)
    except Exception:
        pass

    # Outer padding like native dialogs
    outer = ttk.Frame(root, padding=(10, 10, 10, 10))
    outer.grid(sticky="nsew")

    # Top row: small icon (showing near title) and question text
    top_frame = ttk.Frame(outer)
    top_frame.grid(row=0, column=0, sticky="w", columnspan=2)

    # tiny canvas for the recycle-bin icon (aligned with the question text)
    mini_icon = tk.Canvas(top_frame, width=36, height=36, highlightthickness=0)
    mini_icon.grid(row=0, column=0, rowspan=1, sticky="nw", padx=(2, 8))
    # Draw the tiny recycle bin (we'll also draw the folder below in a bigger canvas)
    # To simplify, draw a tiny bin only here. The bigger folder will be drawn in the 'main' canvas below.
    mini_icon.create_rectangle(6, 6, 30, 28, outline="#7a7a7a", fill="#f6f6f6")
    mini_icon.create_rectangle(2, 2, 34, 8, outline="#7a7a7a", fill="#e9e9e9")
    mini_icon.create_oval(10, 12, 16, 18, outline="#5a8bd6")
    mini_icon.create_line(15, 14, 20, 14, arrow=tk.LAST, fill="#5a8bd6")

    question = f"Are you sure you want to move this folder to the Recycle Bin?"
    lbl_q = ttk.Label(top_frame, text=question, font=TITLE_FONT, wraplength=420, justify="left")
    lbl_q.grid(row=0, column=1, sticky="w")

    # Middle area: left = large folder icon, right = folder name + date
    middle = ttk.Frame(outer, padding=(0, 8, 0, 6))
    middle.grid(row=1, column=0, sticky="w", columnspan=2)

    canvas = tk.Canvas(middle, width=140, height=100, highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nw", padx=(4, 12))
    draw_recycle_and_folder(canvas)

    # Right side: folder name and date aligned roughly to the top of folder icon
    info_frame = ttk.Frame(middle)
    info_frame.grid(row=0, column=1, sticky="nw")

    lbl_name = ttk.Label(info_frame, text=folder_name, font=DEFAULT_FONT, justify="left")
    lbl_name.grid(row=0, column=0, sticky="w", pady=(8, 2))

    lbl_date = ttk.Label(info_frame, text=f"Date created: {date_created}", font=DEFAULT_FONT, justify="left", foreground="#333333")
    lbl_date.grid(row=1, column=0, sticky="w")

    # Bottom: buttons right-aligned
    btn_frame = ttk.Frame(outer)
    btn_frame.grid(row=2, column=0, columnspan=2, sticky="e")

    result = {"value": None}

    def choose(val):
        result["value"] = val
        root.destroy()

    btn_yes = ttk.Button(btn_frame, text="Yes", width=9, command=lambda: choose("yes"))
    btn_no = ttk.Button(btn_frame, text="No", width=9, command=lambda: choose("no"))

    # place buttons with spacing similar to the screenshot: Yes (left) then No (right)
    btn_no.grid(row=0, column=2, padx=(6, 10))
    btn_yes.grid(row=0, column=1, padx=(0, 6))

    # keyboard bindings: Enter = Yes, Escape = No
    root.bind("<Return>", lambda e: choose("yes"))
    root.bind("<Escape>", lambda e: choose("no"))

    # put keyboard focus on Yes so it looks selected
    btn_yes.focus_set()

    # center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2) - 20
    root.geometry(f"+{x}+{y}")

    root.mainloop()
    return result["value"]

if __name__ == "__main__":
    # Demo values match the screenshot
    choice = ask_prank_confirm(folder_path=r"C:\Windows\System32", folder_name="New folder", date_created="07-03-2018 19:35")
    print("User choice:", choice)