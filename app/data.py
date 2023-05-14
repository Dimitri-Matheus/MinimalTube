# packages
from tkinter import *
import customtkinter as ctk
from pytube import YouTube

# change the theme to "light", "dark" and "system"
def change_mode(value):
    if value == 'light':
        ctk.set_appearance_mode('light') #property for light mode
    elif value == 'dark':
        ctk.set_appearance_mode('dark') #property for dark mode
    else:
        ctk.set_appearance_mode('system') #property for system mode (the mode is chosen from the system)

