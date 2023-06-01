import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube
import os

# main window
main_window = ttk.Window(title='Youtube Downloader', themename='vapor')
main_window.geometry('600x600')

# title 
title = ttk.Label(text='Youtube Downloader', font= 'Helvetica 20')
title.pack(pady=10)
# entry
link_entry = ttk.Entry(master=main_window)
link_entry.pack(pady=10)

strvar = tk.StringVar()
label1 = ttk.Label(master=main_window, text= 'add path, leave blank for current directory.',
                   font= 'helvetica 10')
destination_entry = ttk.Entry(master=main_window, textvariable=strvar)

label1.pack(pady=10)
destination_entry.pack(pady = 10)


# downloading
def mp3_download():
    link = link_entry.get()                                     # get the link from the entry
    yt = YouTube(link)                                          # Get youtube method from pytube
    video = yt.streams.filter(only_audio=True).first()          # filter for only audio
    destination = r'C:\Users\endri\Music'                       # destination
    out_file = video.download(output_path=destination)          # download the file
    base, ext = os.path.splitext(out_file)                      # split the file name in 'part' and 'extension'
    new_file = base + '.mp3'                                    # new file with mp3 extension
    os.rename(out_file, new_file)                               # rename the file
    print('Downloaded MP3')                                     # print the message
    text = ttk.Label(master=main_window, text=f'{video.title} succsessfuly downloaded', font='helvetica 10')    # label for the message
    text.pack()                                                 # pack the label
    

# events
main_window.bind('<KeyPress-Return>', lambda event: button.invoke())    # binds enter key to the button and its function


# button
button =ttk.Button(text='Download', command=mp3_download)

button.pack(pady=10)

button_folder = ttk.Button(text='open download folder', command=lambda:os.startfile(r'C:\Users\endri\Music'))
button_folder.pack(pady=10)

main_window.mainloop()



'''
next part:
event binding

Widget.bind(event, function)

format: modifier-type-detail

lambda: button.invoke() calls the button's function

.bind(<Motion>) gets mouse updates

.bind(<FocusIn>) gets value if selected field
.bind(<FocusOut>) gets value if deselected field
'''