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

# downloading
def mp3_download():
    link = link_entry.get()
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    destination = '.'
    out_file = video.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Downloaded MP3')
    
# button
button =ttk.Button(text='Download', command=mp3_download)
button.pack(pady=10)


main_window.mainloop()