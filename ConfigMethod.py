import tkinter as tk
import ttkbootstrap as ttk

# every widget can be updated with the config method
main_window = ttk.Window(themename='vapor')
main_window.geometry('500x400')
main_window.title('Label update')

# update function
def update_function():
    print(entry.get())
    label['text'] = entry.get()
    entry['state'] = 'disabled'

# enable entry button
def enable_function():
    label['text'] = 'Update it!'
    entry['state'] = 'enabled'
    
    
# label
label= ttk.Label(master=main_window, text='Update it!')
label.pack(pady=10)

# entry
entry = ttk.Entry(master=main_window)
entry.pack(pady=10)

# button 1
button = ttk.Button(master=main_window, text='Update', command=update_function)
button.pack(pady=10)

# button 2
enable_button = ttk.Button(master=main_window, text='Enable', command=enable_function)
enable_button.pack()
main_window.mainloop()