import tkinter as tk
import ttkbootstrap as ttk

# main app
main_window = ttk.Window(themename='vapor')
main_window.geometry('600x400')
main_window.title('Buttons app')

#button 1 - normal button
def button_1_func():
    pass

button_string = tk.StringVar(value = 'Button 1')
button_1 = ttk.Button(master=main_window,
                      text='Button 1',
                      command=button_1_func,
                      textvariable=button_string)
button_1.pack(pady=10)

# button 2 - check button
check_var = tk.IntVar()
check_button = ttk.Checkbutton(master=main_window,
                               text='Checkbox 1',
                               command=lambda: print(check_var.get()),
                               variable=check_var,
                               onvalue = 10,
                               offvalue = 5)
check_button.pack(pady=10)

# button 3 - radio buttons
radio_var_1 = ttk.StringVar()
radio_button1 = ttk.Radiobutton(
    master=main_window,
    text='Radio Button',
    value = 'radio 1',
    variable=radio_var_1,
    command=lambda:print(radio_var_1.get()))

radio_button2 = ttk.Radiobutton(
    master=main_window,
    text='Radio Button',
    value = 'radio 2',
    variable=radio_var_1,
    command=lambda:print(radio_var_1.get()))

radio_button1.pack(pady=5)
radio_button2.pack(pady=5)

main_window.mainloop()
