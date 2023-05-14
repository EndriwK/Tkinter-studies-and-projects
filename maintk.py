from tkinter import *
'''from tkinter import ttk'''
import ttkbootstrap as ttk


miles = ''
def convert():
    kms = float(entry_int.get())
    miles = kms * 1.61
    output_string.set(miles)

# window root
root = ttk.Window(themename= 'darkly')
root.title('Tutorial')
root.geometry('800x600')
frm = ttk.Frame(root, padding=10)

# title
title_label = ttk.Label(master=root,  text='Kilometers to Miles', font='helvetica 24')
title_label.pack(pady =10)

#input
input_frame = ttk.Frame(master=root)
entry_int = IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
butt1 = ttk.Button(master = input_frame, text='Convert', command = convert)
entry.pack(side = 'left', padx = 10)
butt1.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = StringVar()
output_label = ttk.Label(master=root,
             text = f'{miles} miles',
             font ='Helvetica 24',
             textvariable = output_string)
output_label.pack(pady=5)

root.mainloop()
