import tkinter as tk
import math

def click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = str(eval(entry.get(), {"__builtins__": None}, math.__dict__))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("TarunTechCalc")
root.geometry("400x600")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["(", ")", "C", "sqrt"],
    ["sin", "cos", "tan", "log"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for text in row:
        btn = tk.Button(frame, text=text, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
