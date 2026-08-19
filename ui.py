import tkinter as tk
from tkinter import messagebox

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
BORDER = "#E2E8F0"
LIGHT_BLUE = "#EFF6FF"
LIGHT_GREEN = "#F0FDF4"

def number(value):
    if value == "":
        return True
    if value.isdigit():
        return True
    messagebox.showerror("Invalid Input", "Numbers only!")
    return False


def text(value):
    if value == "":
        return True
    if all(x.isalpha() or x.isspace() for x in value):
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


def clear():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)

    for entry in a.winfo_children():
        if isinstance(entry, tk.Entry):
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


num = win.register(number)
txt = win.register(text)
dec = win.register(decimal)

# ================= HEADER =================
header = tk.Frame(win, bg=PRIMARY, height=95)
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

main = tk.Frame(win, bg=BG)
main.pack(fill="both", expand=True, padx=35, pady=25)

top = tk.Frame(main, bg=BG)
top.pack(fill="x")

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
s.pack(side="left", fill="both", expand=True, padx=(0, 12))

tk.Label(
    s,
    text="Student ID",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
).grid(row=0, column=0, padx=20, pady=20, sticky="w")

student_id = tk.Entry(
    s,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    fg=TEXT,
    relief="solid",
    bd=1,
    validate="key",
    validatecommand=(num, "%P")
)
student_id.grid(row=0, column=1, padx=10, pady=20, sticky="ew", ipady=7)

tk.Label(
    s,
    text="Student Name",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
).grid(row=1, column=0, padx=20, pady=20, sticky="w")

student_name = tk.Entry(
    s,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    fg=TEXT,
    relief="solid",
    bd=1,
    validate="key",
    validatecommand=(txt, "%P")
)
student_name.grid(row=1, column=1, padx=10, pady=20, sticky="ew", ipady=7)

s.columnconfigure(1, weight=1)

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
a.pack(side="left", fill="both", expand=True, padx=(12, 0))

fields = [
    "Attendance (%)",
    "Study Hours (per day)",
    "Internal Marks (%)",
    "Assignment (%)",
    "Previous Score (%)"
]

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
        pady=10,
        sticky="w"
    )

    tk.Entry(
        a,
        font=("Segoe UI", 12),
        bg="#F8FAFC",
        fg=TEXT,
        relief="solid",
        bd=1,
        validate="key",
        validatecommand=(dec, "%P")
    ).grid(
        row=i,
        column=1,
        padx=10,
        pady=10,
        sticky="ew",
        ipady=5
    )

a.columnconfigure(1, weight=1)

buttons = tk.Frame(main, bg=BG)
buttons.pack(pady=25)

predict_btn = tk.Button(
    buttons,
    text="  Predict Performance  ",
    width=22,
    font=("Segoe UI", 12, "bold"),
    bg=PRIMARY,
    fg="white",
    activebackground=PRIMARY_DARK,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=10
)
predict_btn.pack(side="left", padx=12)

clear_btn = tk.Button(
    buttons,
    text="  Clear  ",
    width=15,
    font=("Segoe UI", 12, "bold"),
    bg=ORANGE,
    fg="white",
    activebackground="#D97706",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=10,
    command=clear
)
clear_btn.pack(side="left", padx=12)

exit_btn = tk.Button(
    buttons,
    text="  Exit  ",
    width=15,
    font=("Segoe UI", 12, "bold"),
    bg=RED,
    fg="white",
    activebackground="#DC2626",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=10,
    command=win.destroy
)
exit_btn.pack(side="left", padx=12)

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
r.pack(fill="x", pady=(0, 10))

tk.Label(
    r,
    text="Prediction",
    font=("Segoe UI", 12, "bold"),
    bg=LIGHT_GREEN,
    fg=TEXT
).grid(row=0, column=0, padx=20, pady=12, sticky="w")

prediction = tk.Entry(
    r,
    font=("Segoe UI", 12),
    bg="white",
    fg=TEXT,
    relief="solid",
    bd=1,
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
).grid(row=1, column=0, padx=20, pady=12, sticky="w")

risk = tk.Entry(
    r,
    font=("Segoe UI", 12),
    bg="white",
    fg=TEXT,
    relief="solid",
    bd=1,
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
).grid(row=2, column=0, padx=20, pady=12, sticky="nw")

recommendation = tk.Text(
    r,
    font=("Segoe UI", 12),
    bg="white",
    fg=TEXT,
    relief="solid",
    bd=1,
    width=70,
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
