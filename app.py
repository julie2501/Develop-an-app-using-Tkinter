import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

window = tk.Tk()
window.title("My App")
window.geometry("200x100")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack()

window.mainloop()
