import tkinter as tk
import ttkbootstrap as ttk
import pafy
import youtube_dl


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
def download():
    video = pafy.new(link)
    best = video.getbest(preftype='mp3')
    print(best.resolution, best.extension)
    best.download
    
link = link_entry.get()


# button
button =ttk.Button(text='Download', command=download)
button.pack(pady=10)


main_window.mainloop()