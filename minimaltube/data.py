# packages
from tkinter import *
import customtkinter as ctk
import webbrowser
from pytube import YouTube
import os
import threading

quality = '360p'

# change the theme
def change_mode(value):
    if value == 'light':
        ctk.set_appearance_mode('light')

    elif value == 'dark':
        ctk.set_appearance_mode('dark')

    else:
        ctk.set_appearance_mode('system')


# attach a link to open in browser
def link(event, var):
    if var == 'GITHUB':
        webbrowser.open_new('https://github.com/Dimitri-Matheus')
        print('link opened success!')

    elif var == 'INSTAGRAM':
        webbrowser.open_new('https://www.instagram.com/dimi_math/')
        print('link opened success!')

    elif var == '':
        webbrowser.open_new('')
        
    else:
        print('ERROR: LINK NOT WORKING!')


# creating a new folder to attach the video files
def create_folder_download(folder_name):
    global new_folder_path

    # get current downloads directory
    current_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    # create the full path to the new folder
    new_folder_path = os.path.join(current_path, folder_name)

    try:
        # create the folder if it doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists.")

        # change downloads directory to new folder
        os.chdir(new_folder_path)
        print(f"Download path changed to '{new_folder_path}'")

    except OSError as e:
        print(f"Error creating folder: {str(e)}")


# function to download videos from youtube using pytube
def data_video(url, state, button, progress_name=0):
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        progress_name.set(percentage)
        progress_name.place(relx=0.4, rely=0.9, anchor=N)
        print(f'Downloading: {percentage:.2f}%', end='\r', flush=True)

    def download():
        global quality
        global new_folder_path

        youtube_var = YouTube(url)

        if state == 0:
            create_folder_download('DOWNLOADED YOUTUBE VIDEOS')
            youtube_var.register_on_progress_callback(on_progress)
            stream = youtube_var.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()
            progress_name.start()
            stream.download(output_path=new_folder_path)

            progress_name.stop()
            progress_name.place_forget()
            button.configure(text='Downloaded!')

            print(f'\nVideo status:\ntitle: {youtube_var.title}\nresolution: {quality}\nthumbnail: {youtube_var.thumbnail_url}')

        # set resolution to 720p
        elif state == 1:
            quality = '720p'
            button.configure(text='Resolution set to 720p')

        # show video title
        elif state == 2:
            button.configure(text=youtube_var.title)

    # Create a new thread for download
    thread = threading.Thread(target=download)
    thread.start()

