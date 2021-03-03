from pygame import mixer
from tkinter import  Tk, Label, Button, filedialog

# screen 

master =Tk()
master.title("Musiflix Player")

Label(master, text="Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0,padx=120)
Label(master, text="Select a track", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1,padx=120)
song_title =Label(master, font =("Calibri",12))
song_title.grid(sticky="N", row =3);
volume_label =Label(master, font =("Calibri",12))
volume_label.grid(sticky="N", row =5);
master.mainloop()