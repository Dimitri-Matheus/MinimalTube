# fuction change page "home", "download" and "setting"
def change_frame(frame_to_show, frames):
    for frame in frames:
        if frame == frame_to_show:
            frame.grid(row=0, column=0, sticky='nsew')
        else:
            frame.grid_forget()


