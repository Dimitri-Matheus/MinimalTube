# packages
from tkinter import *
import customtkinter as ctk
import webbrowser
from pytube import YouTube
import os

#set default resolution
quality = '360p'

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
        webbrowser.open_new('https://github.com/Dimitri-Matheus') #open github link

    elif var == 'INSTAGRAM':
        webbrowser.open_new('https://www.instagram.com/dimi_math/') #open instagram link

    elif var == '':
        webbrowser.open_new('') #open donwload folder
        
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
        print(f"Download path changed to '{new_folder_path}'.")

    except OSError as e:
        print(f"Error creating folder: {str(e)}")


# function to download videos from youtube using pytube
def download_videos(url, state, button):
    global quality
    global new_folder_path

    # get link to youtube videos
    youtube_var = YouTube(url)

    # download videos
    if state == 0:
        create_folder_download('DOWNLOAD YOUTUBE VIDEOS HERE!')
        youtube_var.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first().download(output_path=new_folder_path)
        button.configure(text='Downloaded!')

        # video details
        print(f'Title: {youtube_var.title}\nResolution: {quality}\nThumbnail: {youtube_var.thumbnail_url}')

    # set resolution to 720p
    elif state == 1:
        quality = '720p'
        button.configure(fg_color=('#D9D9D9', '#343638'))
        print(f'resolution set to {quality}')

    # show video title
    elif state == 2:
        button.configure(text=youtube_var.title)

