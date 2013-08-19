from tkinter import *
from sound_pane1 import *
import pygame.mixer

app = Tk()
app.title("Head First Mix")


mixer = pygame.mixer
mixer.init()

create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
create_gui(app, mixer, "49119_M_RED_HardBouncer.wav")


def shutdown():
    track.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()

