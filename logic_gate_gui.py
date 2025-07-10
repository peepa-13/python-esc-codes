import tkinter as tk
from tkinter import messagebox

def NOT(a):
    return not a

def AND(*inputs):
    return all(inputs)

def OR(*inputs):
    return any(inputs)

def NAND(*inputs):
    return not all(inputs)

def NOR(*inputs):
    return not any(inputs)

def XOR(*inputs):
    result = False
    for val in inputs:
        result ^= val
    return result

def XNOR(*inputs):
    return not XOR(*inputs)

gate_funcs = {
    "NOT": NOT,
    "AND": AND,
    "OR": OR,
    "NAND": NAND,
    "NOR": NOR,
    "XOR": XOR,
    "XNOR": XNOR
}

class LogicGateSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Logic Gates Simulator")
        self.geometry("420x500")
        self.configure(padx=20, pady=20)

        self.gate_var = tk.StringVar(value="AND")
        self.input_vars = []
        self.num_inputs = tk.IntVar(value=2)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Logic Gate:").pack()

        gate_menu = tk.OptionMenu(self, self.gate_var, *gate_funcs.keys(), command=self.on_gate_change)
        gate_menu.pack()

        self.input_selector_frame = tk.Frame(self)
        self.input_selector_frame.pack(pady=5)

        tk.Label(self.input_selector_frame, text="Number of Inputs (2-6): ").pack(side="left")
        self.input_spinbox = tk.Spinbox(
            self.input_selector_frame, from_=2, to=6, textvariable=self.num_inputs,
            command=self.update_inputs, width=5
        )
        self.input_spinbox.pack(side="left")

        self.inputs_frame = tk.Frame(self)
        self.inputs_frame.pack(pady=10)

        self.output_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.output_label.pack(pady=10)

        tk.Button(self, text="Compute", command=self.compute).pack()

        self.update_inputs()

    def on_gate_change(self, gate):
        if gate == "NOT":
            self.num_inputs.set(1)
            self.input_spinbox.config(state="disabled")
        else:
            self.num_inputs.set(2)
            self.input_spinbox.config(state="normal")
        self.update_inputs()

    def update_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        self.input_vars = []
        count = self.num_inputs.get()

        for i in range(count):
            var = tk.StringVar(value="0")
            self.input_vars.append(var)
            row = tk.Frame(self.inputs_frame)
            row.pack()
            tk.Label(row, text=f"Input {i+1}: ").pack(side="left")
            tk.Entry(row, textvariable=var, width=5).pack(side="left")

    def compute(self):
        gate = self.gate_var.get()
        func = gate_funcs[gate]
        try:
            inputs = []
            for var in self.input_vars:
                val_str = var.get().strip()
                if val_str == '':
                    raise ValueError("All input fields must be filled.")
                val = int(val_str)
                if val not in [0, 1]:
                    raise ValueError("Inputs must be 0 or 1 only.")
                inputs.append(bool(val))

            if gate == "NOT" and len(inputs) != 1:
                raise ValueError("NOT gate needs exactly 1 input.")
            elif gate != "NOT" and not (2 <= len(inputs) <= 6):
                raise ValueError(f"{gate} gate needs 2–6 inputs.")

            result = func(*inputs)
            binary_inputs = [int(i) for i in inputs]
            self.output_label.config(text=f"{gate}{tuple(binary_inputs)} = {int(result)}")

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

if __name__ == "__main__":
    app = LogicGateSimulator()
    app.mainloop()
