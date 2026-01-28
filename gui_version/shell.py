import tkinter as tk
from tkinter import messagebox, ttk
from dcode import run

def run_interpreter():
    text = entry.get()
    result, error = run('<stdin>', text)
    if error:
        messagebox.showerror("Error", error.as_string())
    else:
        result_label.config(text=str(result))

# Create the main window
root = tk.Tk()
root.title("Dcode Interpreter")
root.geometry("800x400")
root.resizable(False, False)
root.configure(bg="#c3e6f9")  # Set background color to baby blue

# Define colors
bg_color = "#c3e6f9"  # Baby blue
fg_color = "#333333"  # Dark gray
accent_color = "#007bff"  # Blue

# Style for ttk widgets
style = ttk.Style()
style.configure("TLabel", background=bg_color, foreground=fg_color)
style.configure("TButton", background=bg_color, foreground=fg_color, padding=5, bordercolor=bg_color)
style.map("TButton", background=[("active", "#0056b3")])

# Input entry field
entry_label = ttk.Label(root, text="Enter code")
entry_label.pack(pady=5)
entry = ttk.Entry(root, width=100)
entry.pack(pady=5)

# Button to run the interpreter
run_button = ttk.Button(root, text="Run", command=run_interpreter)
run_button.pack(pady=5)

# Result label
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
