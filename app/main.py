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
mercury = '#EBEBEB'
gray_light = '#D9D9D9'


# the window
class MinimalTube(ctk.CTk):
    def __init__(self):
        super().__init__()

        # property the window
        self.title('')
        self.geometry('480x250')
        self.resizable(width=False, height=False)

        # property the dark mode and light mode
        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

        # load the images
        self.arrow = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/push.png'), light_image=PIL.Image.open('images/light/push.png'), size=(45, 45))
        self.github = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/github.png'), light_image=PIL.Image.open('images/light/github.png'), size=(32, 32))
        self.instagram = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/instagram.png'), light_image=PIL.Image.open('images/light/instagram.png'), size=(32, 32))
        self.share = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/share.png'), light_image=PIL.Image.open('images/light/share.png'), size=(32, 32))

        self.find = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/search.png'), light_image=PIL.Image.open('images/light/search.png'), size=(32, 32))
        self.resolution = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/hd.png'), light_image=PIL.Image.open('images/light/hd.png'), size=(32, 32))
        self.download = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/download.png'), light_image=PIL.Image.open('images/light/download.png'), size=(32, 32))

        self.refresh = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/refresh.png'), light_image=PIL.Image.open('images/light/refresh.png'), size=(32, 32))
        self.dark = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/moon.png'), light_image=PIL.Image.open('images/light/moon.png'), size=(32, 32))
        self.light = ctk.CTkImage(dark_image=PIL.Image.open('images/dark/sun.png'), light_image=PIL.Image.open('images/light/sun.png'), size=(32, 32))

        # next page
        self.button_push = ctk.CTkButton(self, text=None, image=self.arrow, fg_color='transparent', hover=False, command=lambda: print('button pressed!'))
        self.button_push.place(relx=1, rely=0.75, anchor=E)

        # buttons social media
        self.button_github = ctk.CTkButton(self, text=None, image=self.github, height=80, width=80)
        self.button_github.configure(fg_color=(white, shoe_wax), hover=False, corner_radius=10)
        self.button_github.place(relx=0.2, rely=0.1, anchor=N)

        self.button_instagram = ctk.CTkButton(self, text=None, image=self.instagram, height=80, width=80)
        self.button_instagram.configure(fg_color=(white, shoe_wax), hover=False, corner_radius=10)
        self.button_instagram.place(relx=0.4, rely=0.1, anchor=N)

        self.button_share = ctk.CTkButton(self, text=None, image=self.share, height=80, width=80)
        self.button_share.configure(fg_color=(white, shoe_wax), hover=False, corner_radius=10)
        self.button_share.place(relx=0.6, rely=0.1, anchor=N)

        # about the project
        self.title = ctk.CTkLabel(self, text='Name the project', text_color=(shoe_wax, white), font=ctk.CTkFont(size=16, weight='bold'))
        self.title.place(relx=0.4, rely=0.5, anchor=N)

        self.description = ctk.CTkLabel(self, text='Lorem Ipsum is simply\n dummy text of the printing\n and typesetting industry.', font=ctk.CTkFont(size=12, weight='bold'), justify='center')
        self.description.configure(width=65, height=65, corner_radius=10, fg_color=(white, shoe_wax), text_color=(shoe_wax, white))
        self.description.place(relx=0.4, rely=0.75, anchor=CENTER)

    # Add icon to window
    def iconbitmap(self, bitmap):
        self._iconbitmap_method_called = False
        super().wm_iconbitmap('images/icon/video.ico')


if __name__ == "__main__":
    app = MinimalTube()
    app.mainloop()