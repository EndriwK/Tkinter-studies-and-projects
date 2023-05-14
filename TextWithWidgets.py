import tkinter as tk
import ttkbootstrap as ttk

# main window parameters
main_window = ttk.Window(themename='vapor')
main_window.title('Widgets and stuff')
main_window.geometry('400x400')

# widget 1 - title
title = tk.Label(master = main_window, text = 'Title', font = 'Helvetica 24 bold')
title.pack()

# widget 2 - text editor
text_box = ttk.Text(master=main_window)
text_box.pack()
# widget 3 - input box
input_box = ttk.Frame(master=main_window)
input_text = tk.StringVar()
input_box_text = ttk.Entry(master=input_box, textvariable= input_text)
input_box.pack(pady = 5)
input_box_text.pack(pady = 5)

# widget 4 - button
def print1():
    print('Button pressed.')

button = ttk.Button(master=main_window, text='Button', command=print1)
button.pack(pady = 5)
main_window.mainloop()

 # widgets are building blocks for tkinter
 # there are tk (old and 90s) and ttk (more modern) widgets
 # .pack() method places widgets from top to bottom
