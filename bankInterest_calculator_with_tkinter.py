# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:24:32 2024

@author:  Sourav Adhikary
"""

import tkinter as tk
from tkinter import messagebox

def calculate_profit():
    try:
        # Get user input
        deposit = float(deposit_entry.get())
        interest_rate = float(rate_entry.get())
        duration = float(duration_entry.get())
        interest_type = interest_type_var.get()
        
        # Validate input
        if deposit <= 0 or interest_rate <= 0 or duration <= 0:
            raise ValueError("All inputs must be positive numbers.")
        
        # Calculate profit
        if interest_type == "Simple":
            profit = deposit * (interest_rate / 100) * duration
            total_amount = deposit + profit
        elif interest_type == "Compound":
            total_amount = deposit * (1 + interest_rate / 100) ** duration
            profit = total_amount - deposit
        else:
            raise ValueError("Invalid interest type selected.")
        
        # Display results
        result_label.config(
            text=f"Total Profit: {profit:.2f}\nTotal Amount: {total_amount:.2f}"
        )
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Banking Profit Calculator")

# Create and place widgets
tk.Label(root, text="Deposit Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
deposit_entry = tk.Entry(root)
deposit_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Duration (Years):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
duration_entry = tk.Entry(root)
duration_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Interest Type:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
interest_type_var = tk.StringVar(value="Simple")
tk.Radiobutton(root, text="Simple", variable=interest_type_var, value="Simple").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Compound", variable=interest_type_var, value="Compound").grid(row=3, column=2, sticky="w")

calculate_button = tk.Button(root, text="Calculate Profit", command=calculate_profit)
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
