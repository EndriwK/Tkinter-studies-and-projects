import tkinter as tk
import ttkbootstrap as ttk
import openai
from AiKey import aikey


# open ai parameters:
openai.api_key = aikey
def gpt_func(input):
    output = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'user',
                    'content': input
        }]
    )
    global gpt_final
    gpt_final = output.choices[0].message.content + '\n'
    print(gpt_final)


# main window
main_window = ttk.Window(themename = 'darkly')
main_window.geometry('800x600')
main_window.title('Chat GPT 3.5')

# title label
title = ttk.Label(master=main_window, text='GPT 3.5', font='Helvetica 24 bold')
title.pack(pady=5)

# text entry
gpt_entry = ttk.Text(master=main_window, width=400, height=5)
gpt_entry.pack(pady=5, padx=5)

# button
def button_func():
    gpt_input = gpt_entry.get('1.0', 'end')
    print(f'final text: {gpt_input}')
    gpt_func(gpt_input)

button = ttk.Button(master=main_window, text='Complete', command= button_func)
button.pack(pady=5)

# label 
complete_gpt = ttk.Label(master=main_window,
                            text=gpt_final,
                            font='helvetica 10 bold',
                            wraplength=800)
complete_gpt.pack()

# main loop
main_window.mainloop()
