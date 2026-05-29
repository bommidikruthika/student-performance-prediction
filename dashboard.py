import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
root.title("Dashboard")
root.geometry("900x600")


# ---------------- SIDEBAR ----------------
menu_frame = tk.Frame(root, bg="lightgray", width=200)
menu_frame.pack(side="left", fill="y")


# ---------------- MAIN DASHBOARD ----------------
dashboard_frame = tk.Frame(root, bg="white")
dashboard_frame.pack(side="right", fill="both", expand=True)


# FIX: force sidebar width to stay visible
menu_frame.pack_propagate(False)


# ---------------- CLEAR FUNCTION ----------------
def clear():
    for w in dashboard_frame.winfo_children():
        w.destroy()


# ---------------- GRAPH ----------------
def show_graph():
    clear()

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    ax.plot(["A", "B", "C"], [10, 20, 30], marker="o")
    ax.set_title("Graph")

    canvas = FigureCanvasTkAgg(fig, dashboard_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# ---------------- PIE ----------------
def show_pie():
    clear()

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    ax.pie([60, 40], labels=["Pass", "Fail"], autopct="%1.1f%%")
    ax.set_title("Pie Chart")

    canvas = FigureCanvasTkAgg(fig, dashboard_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# ---------------- BUTTONS (IMPORTANT FIX HERE) ----------------
tk.Label(menu_frame, text="MENU", bg="lightgray", font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(menu_frame, text="Show Graph", command=show_graph, width=18).pack(pady=10)
tk.Button(menu_frame, text="Pie Chart", command=show_pie, width=18).pack(pady=10)


root.mainloop()