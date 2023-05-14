import tkinter as tk
import ttkbootstrap as ttk

# main window parameters
main_window = ttk.Window(themename='cyborg')
main_window.geometry('800x500')
main_window.title('Text editor')

# save file function
def savefile():
    edited_txt = text_editor.get('1.0', 'end')
    print(f'final text: {edited_txt}')
    file_name = entry_string.get()
    print(f'file name: {file_name}')
    with open(f'{file_name}.txt', 'w') as f:
        f.write(edited_txt)

# text editor
text_editor = ttk.Text(master=main_window, height=8)
text_editor.pack()

# file name entry
title = ttk.Label(master = main_window, text='File name', font='helvetica 14 bold')
title.pack(pady=5)
entry_string = tk.StringVar()
entry_name = ttk.Entry(master=main_window, textvariable=entry_string)
entry_name.pack(pady=5)

# save file button
save_button = ttk.Button(master=main_window, text='save file', command=savefile)
save_button.pack(pady=5)

# main loop
main_window.mainloop()

# .get() method for text accepts 2 arguments get('1.0', 'end')
# for example will get a string from line(1).character(0) til the end
# of the textbox
# open('filename.txt', 'mode (w, a, + )') as x:
#   x.write(content)
