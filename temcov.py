import tkinter as tk
from tkinter import messagebox

BG = "#1e1e2e"
FG = "white"


def convert():
    try:
        temperature = float(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter degrees in figures")
        return

    if unit.get() == "K":
        converted = temperature + 273.15
        text = f"Temperature in Kelvin: {converted:.2f}"
    else:
        converted = temperature * 1.8 + 32
        text = f"Temperature in Fahrenheit: {converted:.2f}"

    if health.get():
        if temperature < 35:
            text += "\nHealth wise: Hypothermia - seek medical advice 🙄🙄"
        elif temperature < 36.1:
            text += "\nHealth wise: Slightly low"
        elif temperature <= 37.2:
            text += "\nHealth wise: Normal"
        elif temperature < 38:
            text += "\nHealth wise: Slightly elevated"
        elif temperature < 39:
            text += "\nHealth wise: Low-grade fever"
        else:
            text += "\nHealth wise: High fever - seek medical advice"

    if temperature >= 38:
        result.config(text=text, fg="yellow")
    else:
        result.config(text=text, fg="lightgreen")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x350")
root.configure(bg=BG)

tk.Label(root, text="Your temperature in Celsius:", bg=BG, fg=FG).pack(pady=(15, 5))
entry = tk.Entry(root)
entry.pack()

unit = tk.StringVar(value="K")
tk.Radiobutton(root, text="Kelvin (K)", variable=unit, value="K",
               bg=BG, fg=FG, selectcolor="#444444",
               activebackground=BG, activeforeground=FG).pack()
tk.Radiobutton(root, text="Fahrenheit (F)", variable=unit, value="F",
               bg=BG, fg=FG, selectcolor="#444444",
               activebackground=BG, activeforeground=FG).pack()

health = tk.BooleanVar()
tk.Checkbutton(root, text="Show health side", variable=health,
               bg=BG, fg=FG, selectcolor="#444444",
               activebackground=BG, activeforeground=FG).pack(pady=5)

tk.Button(root, text="Convert", command=convert,
          bg="green", fg="white", activebackground="darkgreen",
          activeforeground="white").pack(pady=10)

result = tk.Label(root, text="", justify="left", bg=BG, fg="lightgreen")
result.pack()

root.mainloop()