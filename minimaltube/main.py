# packages
from tkinter import *
import customtkinter as ctk
import PIL.Image, PIL.ImageTk
from data import change_mode, link, data_video

class MinimalTube(ctk.CTk):
    def __init__(self):
        super().__init__()

        # property the window
        self.title('')
        self.geometry('480x250')
        self.resizable(width=False, height=False)

        # property the theme
        ctk.set_default_color_theme('minimaltube/themes/default.json')
        ctk.set_appearance_mode('system')

        # load the images
        self.arrow = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/push.png'), light_image=PIL.Image.open('minimaltube/assets/light/push.png'), size=(45, 45))
        self.github = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/github.png'), light_image=PIL.Image.open('minimaltube/assets/light/github.png'), size=(32, 32))
        self.instagram = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/instagram.png'), light_image=PIL.Image.open('minimaltube/assets/light/instagram.png'), size=(32, 32))
        self.folder = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/folder.png'), light_image=PIL.Image.open('minimaltube/assets/light/folder.png'), size=(32, 32))

        self.find = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/search.png'), light_image=PIL.Image.open('minimaltube/assets/light/search.png'), size=(32, 32))
        self.resolution = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/hd.png'), light_image=PIL.Image.open('minimaltube/assets/light/hd.png'), size=(32, 32))
        self.download = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/download.png'), light_image=PIL.Image.open('minimaltube/assets/light/download.png'), size=(32, 32))

        self.refresh = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/refresh.png'), light_image=PIL.Image.open('minimaltube/assets/light/refresh.png'), size=(32, 32))
        self.dark = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/moon.png'), light_image=PIL.Image.open('minimaltube/assets/light/moon.png'), size=(32, 32))
        self.light = ctk.CTkImage(dark_image=PIL.Image.open('minimaltube/assets/dark/sun.png'), light_image=PIL.Image.open('minimaltube/assets/light/sun.png'), size=(32, 32))

        # next page button
        self.button_push = ctk.CTkButton(self, text=None, image=self.arrow, fg_color='transparent', hover=False, command=lambda: change_buttons('video_download'))
        self.button_push.place(relx=1, rely=0.75, anchor=E)

        # default buttons
        self.button_1 = ctk.CTkButton(self, text=None, image=self.github, height=80, width=80, command=lambda: link(self.button_1.bind('<Button-1>'), 'GITHUB'))
        self.button_1.place(relx=0.2, rely=0.1, anchor=N)

        self.button_2 = ctk.CTkButton(self, text=None, image=self.instagram, height=80, width=80, command=lambda: link(self.button_2.bind('<Button-1>'), 'INSTAGRAM'))
        self.button_2.place(relx=0.4, rely=0.1, anchor=N)

        self.button_3 = ctk.CTkButton(self, text=None, image=self.folder, height=80, width=80, command=lambda: link(self.button_2.bind('<Button-1>'), ''))
        self.button_3.place(relx=0.6, rely=0.1, anchor=N)

        # default labels
        self.title = ctk.CTkLabel(self, text='MinimalTube', font=ctk.CTkFont(size=16, weight='bold'))
        self.title.place(relx=0.4, rely=0.5, anchor=N)

        self.description = ctk.CTkLabel(self, text='This program downloads youtube\n videos from a url', font=ctk.CTkFont(size=12, weight='bold'), justify='center')
        self.description.configure(width=65, height=65, corner_radius=10, fg_color=('white', '#2B2B2B'))
        self.description.place(relx=0.4, rely=0.75, anchor=CENTER)

        self.search = ctk.CTkEntry(self, placeholder_text='YOUR URL HERE!', font=ctk.CTkFont(size=14, weight='bold'), width=230, height=40, justify='center')
        self.progress_bar = ctk.CTkProgressBar(self, orientation='horizontal', determinate_speed=5, mode='indeterminate')


        # function to change a page
        def change_buttons(status):
            if status == 'home':
                # buttons
                self.button_1.configure(image=self.github, command=lambda: link(self.button_1.bind('<Button-1>'), 'GITHUB'))
                self.button_2.configure(image=self.instagram, command=lambda: link(self.button_2.bind('<Button-2>'), 'INSTAGRAM'))
                self.button_3.configure(image=self.folder, command=lambda: link(self.button_2.bind('<Button-3>'), ''))

                # about the project
                self.title.configure(text='MinimalTube')
                self.title.place(relx=0.4, rely=0.5, anchor=N)
                self.description.place(relx=0.4, rely=0.75, anchor=CENTER)

                # next page
                self.button_push.configure(command=lambda: change_buttons('video_download'))

            elif status == 'video_download':
                self.button_1.configure(image=self.find, command=lambda: data_video(self.search.get(), 2, self.title))
                self.button_2.configure(image=self.resolution, command=lambda: data_video(self.search.get(), 1, self.title))
                self.button_3.configure(image=self.download, command=lambda: data_video(self.search.get(), 0, self.title, self.progress_bar))

                self.title.configure(text='')
                self.search.place(relx=0.4, rely=0.75, anchor=CENTER)
                self.description.place_forget()
                #self.progress_bar.place(relx=0.4, rely=0.9, anchor=N)

                self.button_push.configure(command=lambda: change_buttons('configuration'))

            elif status == 'configuration':
                self.button_1.configure(image=self.refresh, command=lambda: app.destroy())
                self.button_2.configure(image=self.dark, command=lambda: change_mode('dark'))
                self.button_3.configure(image=self.light, command=lambda: change_mode('light'))

                self.title.configure(text='Settings')
                self.title.place(relx=0.4, rely=0.75, anchor=CENTER)
                self.search.place_forget()
                self.progress_bar.place_forget()

                self.button_push.configure(command=lambda: change_buttons('home'))

            else:
                print('ERROR: NEXT PAGE DOES NOT WORK!')


    # add icon to window
    def iconbitmap(self, bitmap):
        self._iconbitmap_method_called = False
        super().wm_iconbitmap('minimaltube/assets/icon/menu.ico')


if __name__ == "__main__":
    app = MinimalTube()
    app.mainloop()