import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

import os
import sys


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
# LOAD DATASET
# =========================

dataset_path = resource_path("dataset.csv")

data = pd.read_csv(dataset_path)


# Features
X = data[[
    'math',
    'science',
    'english'
]]

# Target
y = data['result']


# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)


# =========================
# PREDICTION FUNCTION
# =========================

def predict_performance(math, science, english):

    prediction = model.predict([
        [math, science, english]
    ])

    return prediction[0]


# =========================
# ACCURACY FUNCTION
# =========================

def get_accuracy():

    return round(
        accuracy * 100,
        2
    )