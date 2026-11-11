import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("450x500")

tk.Label(root, text="Student Registration",
         font=("Arial", 18, "bold")).pack(pady=15)

form = tk.Frame(root)
form.pack(padx=20, fill="both", expand=True)

fields = ["Name", "Student ID", "Email", "Department"]
entries = {}

for i, field in enumerate(fields):
    tk.Label(form, text=field).grid(row=i, column=0, pady=8)
    entries[field] = tk.Entry(form)
    entries[field].grid(row=i, column=1, sticky="ew", pady=8)

tk.Label(form, text="Address").grid(row=4, column=0)
address = tk.Text(form, height=5, width=20)
address.grid(row=4, column=1, pady=8)

form.columnconfigure(1, weight=1)

def save(event=None):
    data = [e.get() for e in entries.values()]
    data.append(address.get("1.0", tk.END).strip())

    if not all(data):
        messagebox.showerror("Error", "Fill all fields!")
        return

    print("Student Information:")
    for field, value in zip(fields + ["Address"], data):
        print(field + ":", value)

    messagebox.showinfo("Success", "Registration Saved!")

def clear(event=None):
    for e in entries.values():
        e.delete(0, tk.END)
    address.delete("1.0", tk.END)

def exit_app(event=None):
    root.destroy()

buttons = tk.Frame(root)
buttons.pack(pady=15)

tk.Button(buttons, text="Save", width=10, command=save).pack(side="left", padx=5)
tk.Button(buttons, text="Clear", width=10, command=clear).pack(side="left", padx=5)
tk.Button(buttons, text="Exit", width=10, command=exit_app).pack(side="left", padx=5)

root.bind("<Return>", save)
root.bind("<Escape>", clear)
root.bind("<Control-s>", save)
root.bind("<Control-S>", save)

root.mainloop()