import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Input features
X = data[
    [
        "Attendance",
        "Study_Hours",
        "Internal_Marks",
        "Assignment",
        "Previous_Score"
    ]
]

# Target
y = data["Performance"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy * 100, "%")

# Classification report
report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save accuracy report
with open("accuracy_report.txt", "w") as file:
    file.write("SMART STUDENT PERFORMANCE PREDICTION SYSTEM\n\n")
    file.write("Model: Random Forest Classifier\n")
    file.write("Accuracy: " + str(round(accuracy * 100, 2)) + "%\n\n")
    file.write("Classification Report:\n")
    file.write(report)

print("\nModel saved as model.pkl")
print("Accuracy report saved as accuracy_report.txt")