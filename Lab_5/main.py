import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Information Form")
root.geometry("450x500")

header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

tk.Label(header, text="Student Information Form",
         font=("Arial", 18, "bold"), bg="lightblue").pack(pady=15)

form = tk.Frame(root, padx=20, pady=20)
form.pack(fill="both", expand=True)

fields = ["Full Name", "Student ID", "Email",
          "Department", "Semester", "Phone"]

entries = {}

for i, field in enumerate(fields):
    tk.Label(form, text=field + ":").grid(row=i, column=0, sticky="w", pady=8)
    entries[field] = tk.Entry(form)
    entries[field].grid(row=i, column=1, sticky="ew", pady=8)

form.columnconfigure(1, weight=1)

def save():
    print("\nStudent Information:")
    for field, entry in entries.items():
        print(field + ":", entry.get())
    messagebox.showinfo("Success", "Information saved!")

def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)

def exit_app():
    root.destroy()

footer = tk.Frame(root)
footer.pack(pady=15)

tk.Button(footer, text="Save", width=10, command=save).pack(side="left", padx=5)
tk.Button(footer, text="Clear", width=10, command=clear).pack(side="left", padx=5)
tk.Button(footer, text="Exit", width=10, command=exit_app).pack(side="left", padx=5)

root.mainloop()
