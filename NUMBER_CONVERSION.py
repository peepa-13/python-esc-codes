import tkinter as tk
from tkinter import ttk, messagebox

# Function to handle conversion
def convert_number():
    input_value = entry.get().strip()
    from_base = base_map[from_var.get()]
    to_base = base_map[to_var.get()]

    try:
        # Convert input to decimal first
        decimal_value = int(input_value, from_base)

        # Convert decimal to target base
        if to_base == 2:
            result = bin(decimal_value)[2:]
        elif to_base == 8:
            result = oct(decimal_value)[2:]
        elif to_base == 10:
            result = str(decimal_value)
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()

        output_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", f"Please enter a valid {from_var.get()} number.")

# Mapping for bases
base_map = {
    "Binary": 2,
    "Octal": 8,
    "Decimal": 10,
    "Hexadecimal": 16
}

# GUI setup
root = tk.Tk()
root.title("Number System Converter")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Number System Converter", font=("Helvetica", 16)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
from_var = tk.StringVar(value="Decimal")
from_menu = ttk.Combobox(frame, textvariable=from_var, values=list(base_map.keys()), state="readonly")
from_menu.grid(row=0, column=1)

tk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
to_var = tk.StringVar(value="Binary")
to_menu = ttk.Combobox(frame, textvariable=to_var, values=list(base_map.keys()), state="readonly")
to_menu.grid(row=0, column=3)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)
entry.insert(0, "Enter number")

convert_btn = tk.Button(root, text="Convert", command=convert_number)
convert_btn.pack(pady=5)

output_label = tk.Label(root, text="Result: ", font=("Helvetica", 14))
output_label.pack(pady=10)

root.mainloop()
