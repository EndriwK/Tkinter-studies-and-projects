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
    link = link_entry.get()
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    destination = r'C:\Users\endri\Music'
    out_file = video.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Downloaded MP3')
    text = ttk.Label(master=main_window, text=f'{video.title} succsessfuly downloaded', font='helvetica 10')
    text.pack()
    
# button
button =ttk.Button(text='Download', command=mp3_download)
button.pack(pady=10)

button_folder = ttk.Button(text='open download folder', command=lambda:os.startfile(r'C:\Users\endri\Music'))
button_folder.pack(pady=10)

main_window.mainloop()
