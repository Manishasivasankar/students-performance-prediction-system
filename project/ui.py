import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Smart Student Performance Prediction System")
win.state("zoomed")
win.configure(bg="#EAF2F8")


# ---------------- VALIDATION ----------------

def number(value):
    if value == "" or value.isdigit():
        return True
    messagebox.showerror("Invalid Input", "Numbers only!")
    return False


def text(value):
    if value == "" or all(x.isalpha() or x.isspace() for x in value):
        return True
    messagebox.showerror("Invalid Input", "Letters only!")
    return False


def decimal(value):
    if value == "":
        return True
    try:
        float(value)
        return True
    except:
        messagebox.showerror("Invalid Input", "Numbers only!")
        return False


num = win.register(number)
txt = win.register(text)
dec = win.register(decimal)


# ---------------- PREDICT ----------------

def predict():

    if student_id.get() == "" or student_name.get() == "" or email.get() == "":
        messagebox.showwarning("Warning", "Please enter all student details!")
        return

    try:
        attendance = float(entries[0].get())
        study = float(entries[1].get())
        internal = float(entries[2].get())
        assignment = float(entries[3].get())
        previous = float(entries[4].get())
    except:
        messagebox.showerror("Error", "Please enter all academic details!")
        return

    if attendance < 0 or attendance > 100:
        messagebox.showwarning("Warning", "Attendance must be between 0 and 100!")
        return

    if study < 0:
        messagebox.showwarning("Warning", "Study hours cannot be negative!")
        return

    if internal < 0 or internal > 100:
        messagebox.showwarning("Warning", "Internal marks must be between 0 and 100!")
        return

    if assignment < 0 or assignment > 100:
        messagebox.showwarning("Warning", "Assignment must be between 0 and 100!")
        return

    if previous < 0 or previous > 100:
        messagebox.showwarning("Warning", "Previous score must be between 0 and 100!")
        return

    score = (
        attendance * 0.20 +
        study * 5 +
        internal * 0.25 +
        assignment * 0.15 +
        previous * 0.20
    )

    if score > 100:
        score = 100

    if score >= 75:
        result = "Excellent Performance"
        risk_level = "Low Risk"
        advice = "Keep up the excellent performance!"

    elif score >= 60:
        result = "Good Performance"
        risk_level = "Medium Risk"
        advice = "Improve your study time and academic performance."

    else:
        result = "Needs Improvement"
        risk_level = "High Risk"
        advice = "Increase study time and focus more on academics."

    prediction.config(state="normal")
    prediction.delete(0, tk.END)
    prediction.insert(0, result)
    prediction.config(state="readonly")

    risk.config(state="normal")
    risk.delete(0, tk.END)
    risk.insert(0, risk_level)
    risk.config(state="readonly")

    recommendation.config(state="normal")
    recommendation.delete("1.0", tk.END)
    recommendation.insert("1.0", advice)
    recommendation.config(state="disabled")


# ---------------- CLEAR ----------------

def clear():

    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    email.delete(0, tk.END)

    for entry in entries:
        entry.delete(0, tk.END)

    prediction.config(state="normal")
    prediction.delete(0, tk.END)
    prediction.config(state="readonly")

    risk.config(state="normal")
    risk.delete(0, tk.END)
    risk.config(state="readonly")

    recommendation.config(state="normal")
    recommendation.delete("1.0", tk.END)
    recommendation.config(state="disabled")


# ---------------- TITLE ----------------

tk.Label(
    win,
    text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",
    font=("Arial", 28, "bold"),
    bg="#EAF2F8",
    fg="#154360"
).pack(pady=25)


# ---------------- MAIN AREA ----------------

main = tk.Frame(win, bg="#EAF2F8")
main.pack(fill="both", expand=True, padx=25)


# ---------------- LEFT SIDE ----------------

left = tk.Frame(main, bg="#EAF2F8")
left.pack(side="left", fill="both", expand=True)


# ---------------- STUDENT INFORMATION ----------------

s = tk.LabelFrame(
    left,
    text="Student Information",
    font=("Arial", 16, "bold"),
    bg="#D6EAF8",
    fg="#154360"
)

s.pack(fill="x", padx=10, pady=5)


tk.Label(s, text="Student ID", font=("Arial", 13), bg="#D6EAF8").grid(
    row=0, column=0, padx=30, pady=18
)

student_id = tk.Entry(
    s,
    font=("Arial", 13),
    validate="key",
    validatecommand=(num, "%P")
)

student_id.grid(row=0, column=1, sticky="ew")


tk.Label(s, text="Student Name", font=("Arial", 13), bg="#D6EAF8").grid(
    row=1, column=0, padx=30, pady=18
)

student_name = tk.Entry(
    s,
    font=("Arial", 13),
    validate="key",
    validatecommand=(txt, "%P")
)

student_name.grid(row=1, column=1, sticky="ew")


tk.Label(s, text="Email ID", font=("Arial", 13), bg="#D6EAF8").grid(
    row=2, column=0, padx=30, pady=18
)

email = tk.Entry(
    s,
    font=("Arial", 13)
)

email.grid(row=2, column=1, sticky="ew")

s.columnconfigure(1, weight=1)


# ---------------- STUDENT PERFORMANCE ----------------

a = tk.LabelFrame(
    left,
    text="Student Performance",
    font=("Arial", 16, "bold"),
    bg="#D6EAF8",
    fg="#154360"
)

a.pack(fill="x", padx=10, pady=5)


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
        font=("Arial", 13),
        bg="#D6EAF8"
    ).grid(row=i, column=0, padx=20, pady=12)

    entry = tk.Entry(
        a,
        font=("Arial", 13),
        validate="key",
        validatecommand=(dec, "%P")
    )

    entry.grid(row=i, column=1, sticky="ew")
    entries.append(entry)

a.columnconfigure(1, weight=1)


# ---------------- BUTTONS ----------------

buttons = tk.Frame(win, bg="#EAF2F8")
buttons.pack(pady=15)


tk.Button(
    buttons,
    text="Predict Performance",
    width=20,
    font=("Arial", 13),
    bg="#3498DB",
    fg="white",
    command=predict
).pack(side="left", padx=15)


tk.Button(
    buttons,
    text="Clear",
    width=12,
    font=("Arial", 13),
    bg="#F39C12",
    fg="white",
    command=clear
).pack(side="left", padx=15)


tk.Button(
    buttons,
    text="Exit",
    width=12,
    font=("Arial", 13),
    bg="#E74C3C",
    fg="white",
    command=win.destroy
).pack(side="left", padx=15)


# ---------------- RIGHT SIDE ----------------

r = tk.LabelFrame(
    main,
    text="Prediction Results",
    font=("Arial", 18, "bold"),
    bg="#D5F5E3",
    fg="#196F3D",
    width=450,
    height=500
)

r.pack(
    side="right",
    fill="both",
    expand=True,
    padx=15,
    pady=5
)

r.pack_propagate(False)


tk.Label(
    r,
    text="Prediction:",
    font=("Arial", 15, "bold"),
    bg="#D5F5E3"
).pack(pady=(45, 10))


prediction = tk.Entry(
    r,
    font=("Arial", 15),
    justify="center",
    state="readonly"
)

prediction.pack(fill="x", padx=40)


tk.Label(
    r,
    text="Risk Level:",
    font=("Arial", 15, "bold"),
    bg="#D5F5E3"
).pack(pady=(30, 10))


risk = tk.Entry(
    r,
    font=("Arial", 15),
    justify="center",
    state="readonly"
)

risk.pack(fill="x", padx=40)


tk.Label(
    r,
    text="Recommendation:",
    font=("Arial", 15, "bold"),
    bg="#D5F5E3"
).pack(pady=(30, 10))


recommendation = tk.Text(
    r,
    font=("Arial", 13),
    height=4,
    state="disabled"
)

recommendation.pack(fill="x", padx=40)


win.mainloop()