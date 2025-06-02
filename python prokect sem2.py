import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, solve, sympify, diff, integrate
import matplotlib.pyplot as plt
import numpy as np

# Main Solver Functions
def solve_equation():
    expr = entry.get()
    try:
        x = symbols('x')
        equation = sympify(expr)
        solutions = solve(equation, x)
        result_text.set(f"Solutions: {solutions}")
    except Exception as e:
        result_text.set(f"Error: {e}")

def differentiate_expression():
    expr = entry.get()
    try:
        x = symbols('x')
        function = sympify(expr)
        derivative = diff(function, x)
        
        result_text.set(f"Derivative: {derivative}")
    except Exception as e:
        result_text.set(f"Error: {e}")

def integrate_expression():
    expr = entry.get()
    try:
        x = symbols('x')
        function = sympify(expr)
        integral = integrate(function, x)
        result_text.set(f"Integral: {integral} + C")
    except Exception as e:
        result_text.set(f"Error: {e}")

def plot_graph():
    expr = entry.get()
    try:
        x = symbols('x')
        function = sympify(expr)

        # Create x and y values
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [float(function.subs(x, val)) for val in x_vals]

        # Plot
        plt.figure(figsize=(6,4))
        plt.plot(x_vals, y_vals, label=f"y = {expr}")
        plt.title("Graph of the Function")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Plot Error", f"Could not plot graph: {e}")

# Build the GUI
app = tk.Tk()
app.title("AI Math Solver")
app.geometry("500x500")
app.configure(bg="#f0f0f0")

# Heading
heading = tk.Label(app, text="🔢 AI Math Solver", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
heading.pack(pady=10)

# Input Field
entry = tk.Entry(app, font=("Arial", 16), width=30, bd=3)
entry.pack(pady=10)

# Buttons Frame
buttons_frame = tk.Frame(app, bg="#f0f0f0")
buttons_frame.pack(pady=10)

solve_btn = tk.Button(buttons_frame, text="Solve Equation", command=solve_equation, width=15, bg="#4CAF50", fg="white", font=("Arial", 12))
solve_btn.grid(row=0, column=0, padx=5, pady=5)

diff_btn = tk.Button(buttons_frame, text="Differentiate", command=differentiate_expression, width=15, bg="#2196F3", fg="white", font=("Arial", 12))
diff_btn.grid(row=0, column=1, padx=5, pady=5)

integrate_btn = tk.Button(buttons_frame, text="Integrate", command=integrate_expression, width=15, bg="#FF5722", fg="white", font=("Arial", 12))
integrate_btn.grid(row=1, column=0, padx=5, pady=5)

graph_btn = tk.Button(buttons_frame, text="Plot Graph", command=plot_graph, width=15, bg="#9C27B0", fg="white", font=("Arial", 12))
graph_btn.grid(row=1, column=1, padx=5, pady=5)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 14), wraplength=400, bg="#f0f0f0", fg="#555")
result_label.pack(pady=20)

# Footer
#footer = tk.Label(app, text="Developed by AI 💻", font=("Arial", 10), bg="#f0f0f0", fg="#999")
#footer.pack(side="bottom", pady=10)

# Run the App
app.mainloop()
