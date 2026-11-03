import tkinter as tk

#window configuration
window = tk.Tk()
window.title("Calculator")
window.geometry("400x515")
window.iconbitmap("calculator(1).ico")
window.config(bg ="#1e1e1e")
window.resizable(False, False)

#calculator interface
buttons = ["1", "2", "3", "+","4", "5", "6", "-", "7", "8", "9", "*", "C", "0", "=", "/"]

frame = tk.Frame(window, bg="#1e1e1e")
frame.pack(pady=20)

label = tk.Label(frame, text="Calculator", font=("Consolas", 24), bg="#1e1e1e", fg="white")
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

entry = tk.Entry(frame, font=("Arial", 24), bg="#3d3d3d", fg="white", highlightthickness=0, borderwidth=0)
entry.grid(row=1, column=0, columnspan=4, padx=15, pady=5)
btnlist = []
for i in range(4):
    for j in range(4):
        if buttons[i*4+j] == "C":
            button = tk.Button(frame, text=buttons[i*4+j], font=("Arial", 24), bg="#FF0000", fg="white", width=3, height=1, highlightthickness=0, borderwidth=0)
        elif buttons[i*4+j] == "=":
            button = tk.Button(frame, text=buttons[i*4+j], font=("Arial", 24), bg="#00FF00", fg="white", width=3, height=1, highlightthickness=0, borderwidth=0)
        else:
             button = tk.Button(frame, text=buttons[i*4+j], font=("Arial", 24), bg="#1e1e1e", fg="white", width=3, height=1, highlightthickness=0, borderwidth=0)
        button.grid(row=i+2, column=j, padx=5, pady=5)
        btnlist.append(button)
label = tk.Label(frame, text="Made by: Habibzada Ilkin", font=("Arial", 12), bg="#1e1e1e", fg="white")
label.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

#calculator functionality
def insert(value):
    if "Error" in entry.get():
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)
    else:
        entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

for button in btnlist:
    if button["text"] == "C":
        button.config(command=clear)
    elif button["text"] == "=":
        button.config(command=calculate)
    else:
        button.config(command=lambda value=button["text"]: insert(value))

#extra widgets animation
def on_enter(e):
    if e.widget["text"] == "C":
        e.widget.config(bg="#FF7F7F")
    elif e.widget["text"] == "=":
        e.widget.config(bg="#7FFF7F")
    else:
        e.widget.config(bg="#3e3e3e")
def on_leave(e):
    if e.widget["text"] == "C":
        e.widget.config(bg="#FF0000")
    elif e.widget["text"] == "=":
        e.widget.config(bg="#00FF00")
    else:
        e.widget.config(bg="#1e1e1e")
def on_press(e):
    e.widget.config(bg="#5e5e5e")

for button in btnlist:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.bind("<Button-1>", on_press)

window.mainloop()
