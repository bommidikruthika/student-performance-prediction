## Student Performance Prediction System
 Overview

The Student Performance Prediction System is a machine learning-based desktop application developed using Python.
It predicts student academic performance based on input data and provides meaningful insights through interactive visualizations.

The application is built with a Tkinter GUI and integrates data processing, machine learning, and data visualization into a single system.

## Features
Secure user login system
Student data entry interface
Machine learning-based performance prediction
Data preprocessing and analysis
Interactive graphs and charts (Matplotlib)
Pie chart visualization
Dataset management and storage
User-friendly desktop GUI using Tkinter

## Technologies Used
Python
Tkinter (GUI Development)
Pandas (Data Processing)
NumPy (Numerical Computation)
Matplotlib (Data Visualization)
Scikit-learn (Machine Learning)

## Project Structure
student_performance_prediction/
│── main.py
│── login_page.py
│── dashboard.py
│── prediction.py
│── data_entry.py
│── data_analysis.py
│── visualization.py
│── utils.py
│── model.pkl
│── dataset.csv
│── students_results.csv
│── logo.png

## Installation & Execution
1. Clone the repository
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
2. Install dependencies
pip install -r requirements.txt
3. Run the application
python main.py

# Modules
Login Module

Handles authentication before accessing the system.

# Data Entry Module

Allows input of student academic records.

# Prediction Module

Uses a trained ML model to predict student performance.

# Visualization Module

Displays graphical insights using charts and graphs.

## Objective

To build an intelligent system that predicts student academic performance and assists in educational decision-making using machine learning.

## Screenshots

Add screenshots of:
1. LOGIN
<img width="1915" height="1079" alt="LOGIN" src="https://github.com/user-attachments/assets/bf6bdc10-8ba2-4819-ba42-e2b6e8885cfe" />
2. DASHBOARD
<img width="1903" height="1063" alt="DASHBOARD (2)" src="https://github.com/user-attachments/assets/73f6fb99-976a-437b-bfd7-aa4d6ba1db77" />
3. PREDICTION
<img width="1909" height="1067" alt="Prediction Output" src="https://github.com/user-attachments/assets/d765d86c-4cca-4eea-a33e-ce85889ecca9" />
4.GRAPH
<img width="1914" height="1073" alt="GRAPH" src="https://github.com/user-attachments/assets/77a38446-f0bd-4a83-9134-8e918017a622" />


## Future Enhancements
Integration with database (MySQL / SQLite)
Improved ML accuracy with advanced models
Web-based version using Flask/Django
Role-based access control system
