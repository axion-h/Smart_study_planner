import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from datetime import datetime, timedelta

# ---------------- Smart Study Planner Logic ---------------- #
subjects = []

def add_subject():
    name = subject_entry.get()
    date = date_entry.get_date()
    if not name:
        messagebox.showerror("Error", "Enter subject name!")
        return
    subjects.append({'name': name, 'date': date})
    update_subject_list()
    subject_entry.delete(0, tk.END)

def update_subject_list():
    subject_list.delete(0, tk.END)
    for i, subject in enumerate(subjects):
        subject_list.insert(tk.END, f"{subject['name']} - {subject['date'].strftime('%d %b %Y')}")
        subject_list.itemconfig(i, {'bg': '#FFEBEE' if i % 2 == 0 else '#FFFFFF'})
        delete_button = tk.Button(subject_list, text="🗑️", command=lambda i=i: delete_subject(i))
        subject_list.window_create(i, window=delete_button)

def delete_subject(index):
    del subjects[index]
    update_subject_list()

def generate_plan():
    if not subjects:
        messagebox.showerror("Error", "Add at least one subject.")
        return
    
    try:
        daily_hours = float(hours_entry.get())
        if daily_hours <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter valid daily study hours.")
        return

    subjects_sorted = sorted(subjects, key=lambda x: x['date'])

    today = datetime.today().date()
    plan = {}
    total_days = 0

    for subj in subjects_sorted:
        days_left = (subj['date'] - today).days
        if days_left <= 0:
            continue
        total_days += days_left
        plan[subj['name']] = days_left

    output.delete(1.0, tk.END)
    output.insert(tk.END, "📚 Smart Study Plan:\n\n")

    for i in range(7):
        output.insert(tk.END, f"📅 {today + timedelta(days=i)}\n")
        for subj, days in plan.items():
            share = days / total_days
            time_for_subj = round(daily_hours * share, 2)
            output.insert(tk.END, f"  - {subj}: {time_for_subj} hours\n")
        output.insert(tk.END, "\n")

def save_plan():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                     filetypes=[("Text files", "*.txt")])
    if file:
        content = output.get(1.0, tk.END)
        file.write(content)
        file.close()
        messagebox.showinfo("Saved", "Plan saved successfully!")

# ---------------- Pomodoro Timer Logic ---------------- #
pomodoro_running = False
pomodoro_seconds = 1500  # 25 minutes

def update_timer():
    global pomodoro_seconds
    if pomodoro_running:
        mins, secs = divmod(pomodoro_seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        if pomodoro_seconds > 0:
            pomodoro_seconds -= 1
            app.after(1000, update_timer)
        else:
            messagebox.showinfo("Pomodoro Complete", "Time for a break!")

def start_timer():
    global pomodoro_running
    if not pomodoro_running:
        pomodoro_running = True
        update_timer()

def stop_timer():
    global pomodoro_running
    pomodoro_running = False

def reset_timer():
    global pomodoro_seconds, pomodoro_running
    pomodoro_running = False
    pomodoro_seconds = 1500
    timer_label.config(text="25:00")

# ---------------- GUI Layout ---------------- #
app = tk.Tk()
app.title("Smart Study Planner with Pomodoro")
app.geometry("700x750")
app.resizable(False, False)

title = tk.Label(app, text="📚 Smart Study Planner", font=("Helvetica", 20, "bold"), bg="#FF7043", fg="white", pady=10)
title.pack(fill='x')

frame = tk.Frame(app)
frame.pack()

subject_entry = tk.Entry(frame, width=20, font=("Arial", 12), bd=2, relief="solid")
subject_entry.grid(row=0, column=0, padx=5)
date_entry = DateEntry(frame, width=15, font=("Arial", 12), date_pattern='yyyy-mm-dd', bd=2, relief="solid")
date_entry.grid(row=0, column=1, padx=5)
add_btn = tk.Button(frame, text="Add Subject", command=add_subject, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="solid")
add_btn.grid(row=0, column=2, padx=5)

subject_list = tk.Listbox(app, width=50, height=5, font=("Arial", 12), selectmode=tk.SINGLE, bd=2, relief="solid")
subject_list.pack(pady=10)

hours_label = tk.Label(app, text="Available Study Hours per Day:", font=("Arial", 12))
hours_label.pack()
hours_entry = tk.Entry(app, width=10, font=("Arial", 12), bd=2, relief="solid")
hours_entry.pack(pady=5)

gen_btn = tk.Button(app, text="Generate Plan", command=generate_plan, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="solid")
gen_btn.pack(pady=10)

output = tk.Text(app, height=12, width=70, font=("Consolas", 10), bd=2, relief="solid")
output.pack(pady=10)

save_btn = tk.Button(app, text="💾 Save Plan", command=save_plan, bg="#FFC107", fg="black", font=("Arial", 12, "bold"), relief="solid")
save_btn.pack(pady=5)

# Pomodoro Timer Section
timer_frame = tk.LabelFrame(app, text="🧠 Pomodoro Focus Timer", padx=10, pady=10, font=("Arial", 12, "bold"), bg="#FF7043", fg="white")
timer_frame.pack(pady=20)

timer_label = tk.Label(timer_frame, text="25:00", font=("Arial", 32, "bold"), fg="#E53935", bg="#FF7043")
timer_label.pack(pady=10)

btns = tk.Frame(timer_frame)
btns.pack()

start_btn = tk.Button(btns, text="▶ Start", command=start_timer, bg="#4CAF50", fg="white", width=10, relief="solid")
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btns, text="⏸ Stop", command=stop_timer, bg="#FFC107", fg="black", width=10, relief="solid")
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btns, text="🔁 Reset", command=reset_timer, bg="#F44336", fg="white", width=10, relief="solid")
reset_btn.grid(row=0, column=2, padx=5)

app.mainloop()