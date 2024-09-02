import tkinter as tk

def on_button_click():
    name = entry.get()
    label.config(text=f"Привет, {name}")

def clear_entry():
    entry.delete(0, tk.END)

def reset_label():
    label.config(text="Введите в окно свое имя:")

root = tk.Tk()
root.geometry("250x150")
root.title("Ввод и обработка имени")

label = tk.Label(root, text="Введите в окно свое имя:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Ввод", command=on_button_click)
button.pack()

clear_button = tk.Button(root, text="Очистить", command=clear_entry)
clear_button.pack()

reset_button = tk.Button(root, text="Сброс", command=reset_label)
reset_button.pack()

root.mainloop()