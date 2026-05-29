import tkinter as tk

def open_window():
    win = tk.Toplevel()
    win.title("Graphs")
    win.geometry("300x200")

    tk.Label(win, text="Graphs Page Coming Soon").pack(pady=50)