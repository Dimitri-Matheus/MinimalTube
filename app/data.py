# packages
from tkinter import *
import customtkinter as ctk
import webbrowser
from pytube import YouTube

# change the theme to "light", "dark" and "system"
def change_mode(value):
    if value == 'light':
        ctk.set_appearance_mode('light') #property for light mode

    elif value == 'dark':
        ctk.set_appearance_mode('dark') #property for dark mode

    else:
        ctk.set_appearance_mode('system') #property for system mode (the mode is chosen from the system)


# attach a link to open in browser
def link(event, var):
    if var == 'GITHUB':
        webbrowser.open_new('https://github.com/Dimitri-Matheus') #open Github

    elif var == 'INSTAGRAM':
        webbrowser.open_new('https://www.instagram.com/dimi_math/') #open Instagram

    else:
        webbrowser.open_new('') #open Linktree


# function to download videos pytube
def download_videos(url, state, hd, progress):
    # get link to youtube videos
    youtube_var = YouTube(url)

    if state == 0:
        # get video size
        video_size = youtube_var.streams.filter(progressive=True, file_extension='mp4', resolution=hd).first().filesize

        # download video
        stream = youtube_var.streams.filter(progressive=True, file_extension='mp4', resolution=hd).first()
        stream.download(filename="video.mp4", output_path="downloads", on_progress_callback=lambda stream, chunk, bytes_remaining: progress.update(int(100 - (100 * bytes_remaining / video_size))))

        # set progress to 100% when download is complete
        progress.update(100)

        print(f'Resolution: {hd}')
        print('Downloaded video!')

    elif state == 1:
        # show video title
        print(youtube_var.title)

# Main program
#download_videos('https://www.youtube.com/watch?v=-X_yVkQrAXs', 0, '360p')