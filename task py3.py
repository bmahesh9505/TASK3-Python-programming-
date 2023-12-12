import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition (+)":
            result = add(num1, num2)
        elif operation == "Subtraction (-)":
            result = subtract(num1, num2)
        elif operation == "Multiplication (*)":
            result = multiply(num1, num2)
        elif operation == "Division (/)":
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num1.pack()

operations = ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])  # Default operation

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
