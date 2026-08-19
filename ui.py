import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("700x700")
root.configure(bg="#EAF4F4")


def predict():

    student_id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()

    try:
        attendance = float(attendance_entry.get())
        study = float(study_entry.get())
        internal = float(internal_entry.get())
        assignment = float(assignment_entry.get())
        previous = float(previous_entry.get())

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers!"
        )
        return


    if student_id == "" or name == "" or email == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Student ID and Name."
        )
        return

    if attendance < 0 or attendance > 100:
        messagebox.showwarning(
            "Warning",
            "Attendance must be between 0 and 100."
        )
        return

    if study < 0:
        messagebox.showwarning(
            "Warning",
            "Study hours cannot be negative."
        )
        return

    if internal < 0 or internal > 100:
        messagebox.showwarning(
            "Warning",
            "Internal marks must be between 0 and 100."
        )
        return

    if assignment < 0 or assignment > 100:
        messagebox.showwarning(
            "Warning",
            "Assignment must be between 0 and 100."
        )
        return

    if previous < 0 or previous > 100:
        messagebox.showwarning(
            "Warning",
            "Previous score must be between 0 and 100."
        )
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

        prediction = "Excellent Performance"
        risk = "Low Risk"

    elif score >= 60:

        prediction = "Good Performance"
        risk = "Medium Risk"

    else:

        prediction = "Needs Improvement"
        risk = "High Risk"



    result_label.config(
        text=f"Student: {name}\n"
             f"Performance Score: {score:.2f}/100\n\n"
             f"Prediction: {prediction}\n"
             f"Risk Level: {risk}"
    )

def clear():

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    attendance_entry.delete(0, tk.END)
    study_entry.delete(0, tk.END)
    internal_entry.delete(0, tk.END)
    assignment_entry.delete(0, tk.END)
    previous_entry.delete(0, tk.END)

    result_label.config(
        text="Enter student details and click Predict"
    )


tk.Label(
    root,
    text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#EAF4F4",
    fg="#155E75"
).pack(pady=(20, 0))



student_frame = tk.LabelFrame(
    root,
    text="  Student Details  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#155E75",
    padx=20,
    pady=10
)

student_frame.pack(
    padx=40,
    pady=8,
    fill="x"
)




tk.Label(
    student_frame,
    text="Register No",
    bg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


id_entry = tk.Entry(
    student_frame,
    width=35,
    relief="solid"
)

id_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    student_frame,
    text="Student Name",
    bg="white"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


name_entry = tk.Entry(
    student_frame,
    width=35,
    relief="solid"
)

name_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)
tk.Label(
    student_frame,
    text="Email id",
    bg="white"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


email_entry = tk.Entry(
    student_frame,
    width=35,
    relief="solid"
)

email_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)



marks_frame = tk.LabelFrame(
    root,
    text="  Academic Details  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#155E75",
    padx=20,
    pady=10
)

marks_frame.pack(
    padx=40,
    pady=8,
    fill="x"
)



tk.Label(
    marks_frame,
    text="Attendance (%)",
    bg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


attendance_entry = tk.Entry(
    marks_frame,
    width=35,
    relief="solid"
)

attendance_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    marks_frame,
    text="Study Hours per Day",
    bg="white"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


study_entry = tk.Entry(
    marks_frame,
    width=35,
    relief="solid"
)

study_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    marks_frame,
    text="Internal Marks (%)",
    bg="white"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


internal_entry = tk.Entry(
    marks_frame,
    width=35,
    relief="solid"
)

internal_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)

tk.Label(
    marks_frame,
    text="Assignment (%)",
    bg="white"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


assignment_entry = tk.Entry(
    marks_frame,
    width=35,
    relief="solid"
)

assignment_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    marks_frame,
    text="Previous Score (%)",
    bg="white"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


previous_entry = tk.Entry(
    marks_frame,
    width=35,
    relief="solid"
)

previous_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)

button_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)

button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="PREDICT",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#2E8B57",
    fg="white",
    command=predict
).grid(
    row=0,
    column=0,
    padx=8
)

tk.Button(
    button_frame,
    text="CLEAR",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#D9534F",
    fg="white",
    command=clear
).grid(
    row=0,
    column=1,
    padx=8
)

tk.Button(
    button_frame,
    text="EXIT",
    width=12,
    font=("Arial", 10, "bold"),
    bg="#555555",
    fg="white",
    command=root.destroy
).grid(
    row=0,
    column=2,
    padx=8
)


result_frame = tk.LabelFrame(
    root,
    text="  Prediction Result  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#155E75",
    padx=15,
    pady=10
)

result_frame.pack(
    padx=40,
    pady=5,
    fill="x"
)


result_label = tk.Label(
    result_frame,
    text="Enter student details and click Predict",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#333333",
    justify="center"
)

result_label.pack(pady=10)

root.mainloop()