import tkinter as tk

def open_window():
    win = tk.Toplevel()
    win.title("Prediction")
    win.geometry("300x200")

    tk.Label(win, text="ML Prediction Page Coming Soon").pack(pady=50)