# packages
from tkinter import *
import customtkinter as ctk
import PIL.Image, PIL.ImageTk
from data import *

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

        # property the theme
        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('system')

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

        # default button next page
        self.button_push = ctk.CTkButton(self, text=None, image=self.arrow, fg_color='transparent', hover=False, command=lambda: change_buttons('video_download'))
        self.button_push.place(relx=1, rely=0.75, anchor=E)

        # default buttons
        self.button_1 = ctk.CTkButton(self, text=None, image=self.github, height=80, width=80)
        self.button_1.configure(fg_color=(white, shoe_wax), hover_color=(gray_light, gray), corner_radius=10)
        self.button_1.place(relx=0.2, rely=0.1, anchor=N)

        self.button_2 = ctk.CTkButton(self, text=None, image=self.instagram, height=80, width=80)
        self.button_2.configure(fg_color=(white, shoe_wax), hover_color=(gray_light, gray), corner_radius=10)
        self.button_2.place(relx=0.4, rely=0.1, anchor=N)

        self.button_3 = ctk.CTkButton(self, text=None, image=self.share, height=80, width=80)
        self.button_3.configure(fg_color=(white, shoe_wax), hover_color=(gray_light, gray), corner_radius=10)
        self.button_3.place(relx=0.6, rely=0.1, anchor=N)

        # default labels
        self.title = ctk.CTkLabel(self, text='MinimalTube', text_color=(shoe_wax, white), font=ctk.CTkFont(size=16, weight='bold'))
        self.title.place(relx=0.4, rely=0.5, anchor=N)

        self.description = ctk.CTkLabel(self, text='This program downloads youtube\n videos from a url.', font=ctk.CTkFont(size=12, weight='bold'), justify='center')
        self.description.configure(width=65, height=65, corner_radius=10, fg_color=(white, shoe_wax), text_color=(shoe_wax, white))
        self.description.place(relx=0.4, rely=0.75, anchor=CENTER)

        self.search = ctk.CTkEntry(self, placeholder_text='YOUR URL HERE!', font=ctk.CTkFont(size=14, weight='bold'))
        self.search.configure(width=230, height=40, corner_radius=10, justify='center', fg_color=(white, shoe_wax), border_color=(white, shoe_wax), text_color=(shoe_wax, white))
        

        # Function to change a page "home", "video_download" and "configuration"
        def change_buttons(status):
            if status == 'home':
                # buttons
                self.button_1.configure(image=self.github, command=None)
                self.button_2.configure(image=self.instagram, command=None)
                self.button_3.configure(image=self.share, command=None)

                # about the project
                self.title.configure(text='MinimalTube')
                self.title.place(relx=0.4, rely=0.5, anchor=N)
                self.description.place(relx=0.4, rely=0.75, anchor=CENTER)

                # next page
                self.button_push.configure(command=lambda: change_buttons('video_download'))

            elif status == 'video_download':
                # buttons
                self.button_1.configure(image=self.find, command=None)
                self.button_2.configure(image=self.resolution, command=None)
                self.button_3.configure(image=self.download, command=None)

                # about the project
                self.title.configure(text='The video Name')
                self.search.place(relx=0.4, rely=0.75, anchor=CENTER)
                self.description.place_forget()

                # next page
                self.button_push.configure(command=lambda: change_buttons('configuration'))

            elif status == 'configuration':
                # buttons
                self.button_1.configure(image=self.refresh, command=None)
                self.button_2.configure(image=self.dark, command=lambda: change_mode('dark'))
                self.button_3.configure(image=self.light, command=lambda: change_mode('light'))

                # about the project
                self.title.configure(text='Settings')
                self.title.place(relx=0.4, rely=0.75, anchor=CENTER)
                self.search.place_forget()

                # next page
                self.button_push.configure(command=lambda: change_buttons('home'))

            else:
                print('ERRO!')


    # Add icon to window
    def iconbitmap(self, bitmap):
        self._iconbitmap_method_called = False
        super().wm_iconbitmap('images/icon/video.ico')


if __name__ == "__main__":
    app = MinimalTube()
    app.mainloop()