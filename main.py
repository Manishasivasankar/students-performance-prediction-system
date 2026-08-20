import tkinter as tk
from tkinter import messagebox
import csv
import os
import pickle

win = tk.Tk()
win.title("Smart Student Performance Prediction System")
win.state("zoomed")
win.configure(bg="#F4F7FB")

BG = "#F4F7FB"
CARD = "#FFFFFF"
PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"
ORANGE = "#F59E0B"
RED = "#EF4444"
GREEN = "#16A34A"
TEXT = "#1E293B"
SUBTEXT = "#64748B"
LIGHT_GREEN = "#F0FDF4"


# Load trained model

try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except:
    messagebox.showerror(
        "Model Error",
        "Please run trainmodel.py first!"
    )
    win.destroy()
    exit()


def number(value):
    if value == "":
        return True

    if value.isdigit():
        return True

    messagebox.showerror(
        "Invalid Input",
        "Numbers only!"
    )
    return False


def text(value):
    if value == "":
        return True

    if all(x.isalpha() or x.isspace() for x in value):
        return True

    messagebox.showerror(
        "Invalid Input",
        "Letters only!"
    )
    return False


def decimal(value):
    if value == "":
        return True

    try:
        float(value)
        return True
    except:
        messagebox.showerror(
            "Invalid Input",
            "Numbers only!"
        )
        return False


# Prediction

def predict():

    if student_id.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Student ID!"
        )
        return

    if student_name.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Student Name!"
        )
        return

    if email.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Email ID!"
        )
        return

    try:
        attendance = float(attendance_entry.get())
        study = float(study_entry.get())
        internal = float(internal_entry.get())
        assignment = float(assignment_entry.get())
        previous = float(previous_entry.get())

    except:
        messagebox.showerror(
            "Error",
            "Please enter all academic details!"
        )
        return


    if attendance < 0 or attendance > 100:
        messagebox.showwarning(
            "Warning",
            "Attendance must be between 0 and 100!"
        )
        return

    if study < 0 or study > 24:
        messagebox.showwarning(
            "Warning",
            "Study hours must be between 0 and 24!"
        )
        return

    if internal < 0 or internal > 100:
        messagebox.showwarning(
            "Warning",
            "Internal marks must be between 0 and 100!"
        )
        return

    if assignment < 0 or assignment > 100:
        messagebox.showwarning(
            "Warning",
            "Assignment must be between 0 and 100!"
        )
        return

    if previous < 0 or previous > 100:
        messagebox.showwarning(
            "Warning",
            "Previous score must be between 0 and 100!"
        )
        return


    # Give input to trained model

    student_data = [[
        attendance,
        study,
        internal,
        assignment,
        previous
    ]]

    result = model.predict(student_data)[0]


    # Show prediction

    prediction.config(state="normal")
    prediction.delete(0, tk.END)
    prediction.insert(0, result)
    prediction.config(state="readonly")


    if result == "Excellent":

        risk_level = "Low Risk"
        advice = "Excellent performance! Keep up the good work."

    elif result == "Good":

        risk_level = "Medium Risk"
        advice = "Good performance. Try to improve your academic scores."

    else:

        risk_level = "High Risk"
        advice = "Needs improvement. Focus more on your studies."


    risk.config(state="normal")
    risk.delete(0, tk.END)
    risk.insert(0, risk_level)
    risk.config(state="readonly")


    recommendation.config(state="normal")
    recommendation.delete("1.0", tk.END)
    recommendation.insert("1.0", advice)
    recommendation.config(state="disabled")


# Save data

def save_data():

    if prediction.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please click Predict Performance first!"
        )
        return

    file = "student_performance.csv"

    data = [
        student_id.get(),
        student_name.get(),
        email.get(),
        attendance_entry.get(),
        study_entry.get(),
        internal_entry.get(),
        assignment_entry.get(),
        previous_entry.get(),
        prediction.get()
    ]

    with open(file, "a", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(data)

    messagebox.showinfo(
        "Saved",
        "Student data added to dataset!"
    )


# Clear

def clear():

    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    email.delete(0, tk.END)

    attendance_entry.delete(0, tk.END)
    study_entry.delete(0, tk.END)
    internal_entry.delete(0, tk.END)
    assignment_entry.delete(0, tk.END)
    previous_entry.delete(0, tk.END)

    prediction.config(state="normal")
    prediction.delete(0, tk.END)
    prediction.config(state="readonly")

    risk.config(state="normal")
    risk.delete(0, tk.END)
    risk.config(state="readonly")

    recommendation.config(state="normal")
    recommendation.delete("1.0", tk.END)
    recommendation.config(state="disabled")


num = win.register(number)
txt = win.register(text)
dec = win.register(decimal)


# HEADER

header = tk.Frame(
    win,
    bg=PRIMARY,
    height=95
)

header.pack(fill="x")
header.pack_propagate(False)


tk.Label(
    header,
    text="SMART STUDENT",
    font=("Segoe UI", 26, "bold"),
    bg=PRIMARY,
    fg="white"
).pack(pady=(15, 0))


tk.Label(
    header,
    text="PERFORMANCE PREDICTION SYSTEM",
    font=("Segoe UI", 13),
    bg=PRIMARY,
    fg="#DBEAFE"
).pack()


# MAIN

main = tk.Frame(
    win,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=25
)


top = tk.Frame(
    main,
    bg=BG
)

top.pack(fill="x")


# STUDENT INFORMATION

s = tk.LabelFrame(
    top,
    text="  Student Information  ",
    font=("Segoe UI", 15, "bold"),
    bg=CARD,
    fg=PRIMARY,
    bd=1,
    relief="solid",
    padx=20,
    pady=15
)

s.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 12)
)


tk.Label(
    s,
    text="Student ID",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
).grid(
    row=0,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)


student_id = tk.Entry(
    s,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    validate="key",
    validatecommand=(num, "%P")
)

student_id.grid(
    row=0,
    column=1,
    padx=10,
    pady=15,
    sticky="ew",
    ipady=7
)


tk.Label(
    s,
    text="Student Name",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
).grid(
    row=1,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)


student_name = tk.Entry(
    s,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    validate="key",
    validatecommand=(txt, "%P")
)

student_name.grid(
    row=1,
    column=1,
    padx=10,
    pady=15,
    sticky="ew",
    ipady=7
)


tk.Label(
    s,
    text="Email ID",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
).grid(
    row=2,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)


email = tk.Entry(
    s,
    font=("Segoe UI", 12),
    bg="#F8FAFC"
)

email.grid(
    row=2,
    column=1,
    padx=10,
    pady=15,
    sticky="ew",
    ipady=7
)

s.columnconfigure(1, weight=1)


# ACADEMIC INFORMATION

a = tk.LabelFrame(
    top,
    text="  Academic Information  ",
    font=("Segoe UI", 15, "bold"),
    bg=CARD,
    fg=PRIMARY,
    bd=1,
    relief="solid",
    padx=20,
    pady=15
)

a.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(12, 0)
)


fields = [
    "Attendance (%)",
    "Study Hours (per day)",
    "Internal Marks (%)",
    "Assignment (%)",
    "Previous Score (%)"
]


entries = []

for i, field in enumerate(fields):

    tk.Label(
        a,
        text=field,
        font=("Segoe UI", 12),
        bg=CARD,
        fg=TEXT
    ).grid(
        row=i,
        column=0,
        padx=15,
        pady=8,
        sticky="w"
    )

    entry = tk.Entry(
        a,
        font=("Segoe UI", 12),
        bg="#F8FAFC",
        validate="key",
        validatecommand=(dec, "%P")
    )

    entry.grid(
        row=i,
        column=1,
        padx=10,
        pady=8,
        sticky="ew",
        ipady=5
    )

    entries.append(entry)


attendance_entry = entries[0]
study_entry = entries[1]
internal_entry = entries[2]
assignment_entry = entries[3]
previous_entry = entries[4]

a.columnconfigure(1, weight=1)


# BUTTONS

buttons = tk.Frame(
    main,
    bg=BG
)

buttons.pack(pady=20)


tk.Button(
    buttons,
    text="Save",
    width=12,
    font=("Arial", 13),
    bg=GREEN,
    fg="white",
    command=save_data
).pack(
    side="left",
    padx=12
)


tk.Button(
    buttons,
    text="Predict Performance",
    width=22,
    font=("Segoe UI", 12, "bold"),
    bg=PRIMARY,
    fg="white",
    activebackground=PRIMARY_DARK,
    relief="flat",
    command=predict
).pack(
    side="left",
    padx=12
)


tk.Button(
    buttons,
    text="Clear",
    width=15,
    font=("Segoe UI", 12, "bold"),
    bg=ORANGE,
    fg="white",
    relief="flat",
    command=clear
).pack(
    side="left",
    padx=12
)


tk.Button(
    buttons,
    text="Exit",
    width=15,
    font=("Segoe UI", 12, "bold"),
    bg=RED,
    fg="white",
    relief="flat",
    command=win.destroy
).pack(
    side="left",
    padx=12
)


# RESULTS

r = tk.LabelFrame(
    main,
    text="  Prediction Results  ",
    font=("Segoe UI", 15, "bold"),
    bg=LIGHT_GREEN,
    fg=GREEN,
    bd=1,
    relief="solid",
    padx=25,
    pady=15
)

r.pack(
    fill="x",
    pady=(0, 10)
)


tk.Label(
    r,
    text="Prediction",
    font=("Segoe UI", 12, "bold"),
    bg=LIGHT_GREEN,
    fg=TEXT
).grid(
    row=0,
    column=0,
    padx=20,
    pady=12,
    sticky="w"
)


prediction = tk.Entry(
    r,
    font=("Segoe UI", 12),
    bg="white",
    state="readonly"
)

prediction.grid(
    row=0,
    column=1,
    padx=10,
    pady=12,
    sticky="ew",
    ipady=6
)


tk.Label(
    r,
    text="Risk Level",
    font=("Segoe UI", 12, "bold"),
    bg=LIGHT_GREEN,
    fg=TEXT
).grid(
    row=1,
    column=0,
    padx=20,
    pady=12,
    sticky="w"
)


risk = tk.Entry(
    r,
    font=("Segoe UI", 12),
    bg="white",
    state="readonly"
)

risk.grid(
    row=1,
    column=1,
    padx=10,
    pady=12,
    sticky="ew",
    ipady=6
)


tk.Label(
    r,
    text="Recommendation",
    font=("Segoe UI", 12, "bold"),
    bg=LIGHT_GREEN,
    fg=TEXT
).grid(
    row=2,
    column=0,
    padx=20,
    pady=12,
    sticky="nw"
)


recommendation = tk.Text(
    r,
    font=("Segoe UI", 12),
    bg="white",
    height=4,
    state="disabled",
    wrap="word"
)

recommendation.grid(
    row=2,
    column=1,
    padx=10,
    pady=12,
    sticky="ew"
)

r.columnconfigure(1, weight=1)


tk.Label(
    win,
    text="© Smart Student Performance Prediction System",
    font=("Segoe UI", 9),
    bg=BG,
    fg=SUBTEXT
).pack(pady=(0, 8))


win.mainloop()
