# packages
from tkinter import *
import customtkinter as ctk
import PIL.Image, PIL.ImageTk
from pytube import YouTube

# Colors
white = '#FEFFFF'
black = '#000000'
gray = '#343638'
shoe_wax = '#2B2B2B'
young_night = '#242424'
Mercury = '#EBEBEB'
gray_light = '#D9D9D9'


# the window
class MinimalTube(ctk.CTk):
    def __init__(self):
        super().__init__()

        # property the window
        self.title('MinimalTube')
        self.geometry('480x250')
        self.resizable(width=False, height=False)

        # property the dark mode and light mode
        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

if __name__ == "__main__":
    app = MinimalTube()
    app.mainloop()