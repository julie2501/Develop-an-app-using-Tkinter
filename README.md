# Develop-an-app-using-Tkinter

Here's a simple app using Tkinter in repl.it that creates a window with a label and a button:

python code
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
This code defines a function on_button_click that changes the text of the label when the button is clicked. It creates a window with a title of "My App" and dimensions of 200x100 pixels. It then creates a label with the text "Hello, Tkinter!" and a button with the text "Click me!" that calls the on_button_click function when clicked. Finally, it starts the Tkinter event loop by calling window.mainloop(). This app has a total of 9 lines of code.
