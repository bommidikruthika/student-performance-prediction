import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Logo Image
from PIL import Image, ImageTk

# EXE Fix
import os
import sys

# ML Functions
from model import predict_performance, get_accuracy

# Graph
import matplotlib.pyplot as plt

# CSV
import csv

# SQLite Database
import sqlite3

# PDF
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


# =========================
# FIX FOR EXE FILE
# =========================

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_results (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    roll TEXT,

    math INTEGER,

    science INTEGER,

    english INTEGER,

    result TEXT
)
""")

conn.commit()


# =========================
# LOGIN PAGE CLASS
# =========================

class LoginPage:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Student Performance Prediction System"
        )

        self.root.geometry("500x550")

        self.root.configure(bg="#EAF2F8")

        # =========================
        # LOGO IMAGE
        # =========================

        logo_image = Image.open(
            resource_path("logo.png")
        )

        logo_image = logo_image.resize((120, 120))

        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(
            root,
            image=logo_photo,
            bg="#EAF2F8"
        )

        logo_label.image = logo_photo

        logo_label.pack(pady=10)

        # Heading
        tk.Label(
            root,
            text="Student Performance Prediction",
            font=("Arial", 18, "bold"),
            bg="#EAF2F8",
            fg="#1B4F72"
        ).pack(pady=10)

        # Username
        tk.Label(
            root,
            text="Username",
            bg="#EAF2F8",
            font=("Arial", 11)
        ).pack()

        self.username = tk.Entry(
            root,
            width=30
        )

        self.username.pack(pady=5)

        # Password
        tk.Label(
            root,
            text="Password",
            bg="#EAF2F8",
            font=("Arial", 11)
        ).pack()

        self.password = tk.Entry(
            root,
            show="*",
            width=30
        )

        self.password.pack(pady=5)

        # Login Button
        tk.Button(
            root,
            text="Login",
            width=15,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.login
        ).pack(pady=20)

    # =========================
    # LOGIN FUNCTION
    # =========================

    def login(self):

        user = self.username.get()

        pwd = self.password.get()

        if user == "admin" and pwd == "1234":

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            dashboard = tk.Toplevel(self.root)

            dashboard.title("Dashboard")

            dashboard.geometry("750x750")

            dashboard.configure(bg="#F4F6F7")

            # =========================
            # DASHBOARD LOGO
            # =========================

            dash_logo = Image.open(
                resource_path("logo.png")
            )

            dash_logo = dash_logo.resize((80, 80))

            dash_photo = ImageTk.PhotoImage(dash_logo)

            dash_label = tk.Label(
                dashboard,
                image=dash_photo,
                bg="#F4F6F7"
            )

            dash_label.image = dash_photo

            dash_label.pack(pady=10)

            # Heading
            tk.Label(
                dashboard,
                text="Student Performance Prediction",
                font=("Arial", 18, "bold"),
                bg="#F4F6F7",
                fg="#1B4F72"
            ).pack(pady=10)

            # Accuracy
            accuracy = get_accuracy()

            tk.Label(
                dashboard,
                text=f"Model Accuracy: {accuracy}%",
                font=("Arial", 11, "bold"),
                fg="green",
                bg="#F4F6F7"
            ).pack(pady=5)

            # Student Name
            tk.Label(
                dashboard,
                text="Student Name",
                bg="#F4F6F7",
                font=("Arial", 11)
            ).pack()

            name_entry = tk.Entry(
                dashboard,
                width=30
            )

            name_entry.pack(pady=5)

            # Roll Number
            tk.Label(
                dashboard,
                text="Roll Number",
                bg="#F4F6F7",
                font=("Arial", 11)
            ).pack()

            roll_entry = tk.Entry(
                dashboard,
                width=30
            )

            roll_entry.pack(pady=5)

            # Math
            tk.Label(
                dashboard,
                text="Math Marks",
                bg="#F4F6F7",
                font=("Arial", 11)
            ).pack()

            math_entry = tk.Entry(
                dashboard,
                width=30
            )

            math_entry.pack(pady=5)

            # Science
            tk.Label(
                dashboard,
                text="Science Marks",
                bg="#F4F6F7",
                font=("Arial", 11)
            ).pack()

            science_entry = tk.Entry(
                dashboard,
                width=30
            )

            science_entry.pack(pady=5)

            # English
            tk.Label(
                dashboard,
                text="English Marks",
                bg="#F4F6F7",
                font=("Arial", 11)
            ).pack()

            english_entry = tk.Entry(
                dashboard,
                width=30
            )

            english_entry.pack(pady=5)

            # =========================
            # PREDICTION FUNCTION
            # =========================

            def predict():

                try:

                    name = name_entry.get()

                    roll = roll_entry.get()

                    m1 = int(math_entry.get())

                    m2 = int(science_entry.get())

                    m3 = int(english_entry.get())

                    result = predict_performance(
                        m1,
                        m2,
                        m3
                    )

                    # Save CSV
                    with open(
                        "student_results.csv",
                        "a",
                        newline=""
                    ) as file:

                        writer = csv.writer(file)

                        writer.writerow([
                            name,
                            roll,
                            m1,
                            m2,
                            m3,
                            result
                        ])

                    # Save Database
                    cursor.execute(
                        """
                        INSERT INTO student_results
                        (name, roll, math, science, english, result)

                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (
                            name,
                            roll,
                            m1,
                            m2,
                            m3,
                            result
                        )
                    )

                    conn.commit()

                    # PDF
                    doc = SimpleDocTemplate(
                        "student_report.pdf"
                    )

                    styles = getSampleStyleSheet()

                    elements = []

                    elements.append(
                        Paragraph(
                            "Student Performance Report",
                            styles['Title']
                        )
                    )

                    elements.append(
                        Spacer(1, 20)
                    )

                    elements.append(
                        Paragraph(
                            f"Student Name: {name}",
                            styles['BodyText']
                        )
                    )

                    elements.append(
                        Paragraph(
                            f"Roll Number: {roll}",
                            styles['BodyText']
                        )
                    )

                    elements.append(
                        Paragraph(
                            f"Math Marks: {m1}",
                            styles['BodyText']
                        )
                    )

                    elements.append(
                        Paragraph(
                            f"Science Marks: {m2}",
                            styles['BodyText']
                        )
                    )

                    elements.append(
                        Paragraph(
                            f"English Marks: {m3}",
                            styles['BodyText']
                        )
                    )

                    elements.append(
                        Paragraph(
                            f"Prediction Result: {result}",
                            styles['BodyText']
                        )
                    )

                    doc.build(elements)

                    # Result Label
                    result_label.config(
                        text=f"Student: {name}\n"
                             f"Roll No: {roll}\n"
                             f"Prediction: {result}"
                    )

                    # Graph
                    subjects = [
                        "Math",
                        "Science",
                        "English"
                    ]

                    marks = [
                        m1,
                        m2,
                        m3
                    ]

                    plt.figure(figsize=(5, 4))

                    plt.bar(subjects, marks)

                    plt.title(
                        "Student Marks Analysis"
                    )

                    plt.xlabel("Subjects")

                    plt.ylabel("Marks")

                    plt.ylim(0, 100)

                    plt.show()

                    messagebox.showinfo(
                        "Success",
                        "Prediction Completed"
                    )

                except:

                    messagebox.showerror(
                        "Error",
                        "Please enter valid values"
                    )

            # Predict Button
            tk.Button(
                dashboard,
                text="Predict Performance",
                width=22,
                bg="#2ECC71",
                fg="white",
                font=("Arial", 11, "bold"),
                command=predict
            ).pack(pady=20)

            # Result Label
            result_label = tk.Label(
                dashboard,
                text="",
                font=("Arial", 12, "bold"),
                bg="#F4F6F7",
                fg="#1B2631"
            )

            result_label.pack(pady=20)

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )