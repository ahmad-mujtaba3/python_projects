import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Employee Registration")
root.geometry("550x650")

# Header Frame
header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

logo = tk.PhotoImage(width=40, height=40)
tk.Label(header, image=logo, bg="lightblue").pack(side="left", padx=15)

tk.Label(header, text="Employee Registration",
         font=("Arial", 20, "bold"), bg="lightblue").pack(pady=15)

# Form Frame
form = tk.Frame(root, padx=20, pady=15)
form.pack(fill="both", expand=True)

fields = ["Employee ID", "Name", "Email", "Phone", "Position"]
entries = {}

for i, field in enumerate(fields):
    tk.Label(form, text=field, font=("Arial", 11)).grid(
        row=i, column=0, sticky="w", pady=7)
    entries[field] = tk.Entry(form, font=("Arial", 11))
    entries[field].grid(row=i, column=1, sticky="ew", pady=7)

tk.Label(form, text="Address", font=("Arial", 11)).grid(
    row=5, column=0, sticky="nw", pady=7)

address = tk.Text(form, height=4, width=25)
address.grid(row=5, column=1, sticky="ew", pady=7)

form.columnconfigure(1, weight=1)

# Save Function
def save():
    data = {field: entry.get() for field, entry in entries.items()}
    data["Address"] = address.get("1.0", tk.END).strip()

    if not all(data.values()):
        messagebox.showerror("Error", "All fields are required!")
        return

    print("\nEmployee Information:")
    for field, value in data.items():
        print(field + ":", value)

    messagebox.showinfo("Success", "Employee saved!")

# Clear Function
def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)
    address.delete("1.0", tk.END)

# Edit Function
def edit():
    employee_id = entries["Employee ID"].get()

    if not employee_id:
        messagebox.showerror("Error", "Enter Employee ID!")
        return

    save()

# Action Frame
actions = tk.Frame(root)
actions.pack(pady=15)

tk.Button(actions, text="Save", width=12, command=save).pack(side="left", padx=5)
tk.Button(actions, text="Clear", width=12, command=clear).pack(side="left", padx=5)
tk.Button(actions, text="Edit", width=12, command=edit).pack(side="left", padx=5)

# Stats Frame
stats = tk.Frame(root, bg="lightgray")
stats.pack(fill="x")

tk.Label(stats, text="Employee Management System",
         font=("Times New Roman", 11, "italic"),
         bg="lightgray").pack(pady=10)

root.mainloop()