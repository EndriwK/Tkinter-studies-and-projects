import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube


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
    stream = yt.streams.get_audio_only(subtype='mp3')
    stream.download()
    print('Downloaded MP3')
    



# button
button =ttk.Button(text='Download', command=mp3_download)
button.pack(pady=10)


main_window.mainloop()