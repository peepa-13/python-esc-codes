import tkinter as tk
from tkinter import ttk, messagebox

# Define logic gate functions
def AND(*inputs):
    return all(inputs)

def OR(*inputs):
    return any(inputs)

def NOT(a):
    return not a

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

gate_functions = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "NAND": NAND,
    "NOR": NOR,
    "XOR": XOR,
    "XNOR": XNOR
}

# GUI app
class LogicGateSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💖 Logic Gate Simulator 💖")
        self.geometry("500x600")
        self.configure(bg="#ffe6f0")  # Baby pink background

        self.gate_var = tk.StringVar(value="AND")
        self.input_vars = []
        self.num_inputs = tk.IntVar(value=2)

        self.build_gui()

    def build_gui(self):
        font_title = ("Comic Sans MS", 18, "bold")
        font_label = ("Comic Sans MS", 12)
        font_button = ("Comic Sans MS", 11)

        tk.Label(self, text="Logic Gate Simulator", bg="#ffe6f0", fg="#cc0066", font=font_title).pack(pady=20)

        # Gate selector
        frame_top = tk.Frame(self, bg="#ffe6f0")
        frame_top.pack()
        tk.Label(frame_top, text="Gate:", bg="#ffe6f0", font=font_label).pack(side="left")
        ttk.Combobox(frame_top, textvariable=self.gate_var, values=list(gate_functions.keys()),
                     state="readonly", font=font_label, width=10).pack(side="left", padx=10)

        # Input count
        tk.Label(frame_top, text="  Inputs (2–6):", bg="#ffe6f0", font=font_label).pack(side="left")
        self.spinbox = tk.Spinbox(frame_top, from_=2, to=6, textvariable=self.num_inputs, command=self.update_inputs,
                                  font=font_label, width=3)
        self.spinbox.pack(side="left")

        self.inputs_frame = tk.Frame(self, bg="#ffe6f0")
        self.inputs_frame.pack(pady=20)
        self.update_inputs()

        tk.Button(self, text="✨ Compute ✨", command=self.compute,
                  bg="#ff99cc", fg="white", font=font_button, bd=0,
                  activebackground="#ff66a3", activeforeground="white",
                  padx=20, pady=5).pack(pady=15)

        self.output_label = tk.Label(self, text="Result: ", bg="#ffe6f0", font=font_label, fg="#993366")
        self.output_label.pack(pady=10)

        self.gate_var.trace_add("write", lambda *args: self.update_inputs())

    def update_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        self.input_vars = []
        gate = self.gate_var.get()

        if gate == "NOT":
            self.num_inputs.set(1)
            self.spinbox.config(state="disabled")
        else:
            self.spinbox.config(state="normal")

        count = self.num_inputs.get() if gate != "NOT" else 1
        for i in range(count):
            var = tk.StringVar(value="0")
            self.input_vars.append(var)
            row = tk.Frame(self.inputs_frame, bg="#ffe6f0")
            row.pack()
            tk.Label(row, text=f"Input {i + 1}:", bg="#ffe6f0", font=("Comic Sans MS", 11)).pack(side="left")
            tk.Entry(row, textvariable=var, width=5, font=("Comic Sans MS", 11)).pack(side="left")

    def compute(self):
        gate = self.gate_var.get()
        func = gate_functions[gate]
        try:
            inputs = []
            for var in self.input_vars:
                val_str = var.get().strip()
                if val_str not in ["0", "1"]:
                    raise ValueError("Inputs must be 0 or 1")
                inputs.append(bool(int(val_str)))

            if gate == "NOT":
                result = func(inputs[0])
            else:
                result = func(*inputs)

            result_str = f"{gate}{tuple(int(b) for b in inputs)} = {int(result)}"
            self.output_label.config(text="Result: " + result_str)

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = LogicGateSimulator()
    app.mainloop()
