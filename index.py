from pygame import mixer
from tkinter import  Tk, Label, Button, filedialog

default_volume =float(0.5)

# commands
def select_track():
	filename =filedialog.askopenfilename(initialdir="C:/", title ="Please select a song")
	selected_track =filename
	track_title =filename.split("/")
	track_title =track_title[-1]

	try:
		mixer.init()
		mixer.music.load(selected_track)
		mixer.music.set_volume(default_volume)
		mixer.music.play()
		song_title.config(fg="green", text=str(track_title))
		volume_label.config(fg="green", text=str(default_volume))
	except Exception as e:
		print(e)
		song_title.config(fg="red", text="Error, playing track")
		pass

# screen 
master =Tk()
master.title("Musiflix Player")

#labels
Label(master, text="Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0,padx=120)
Label(master, text="Please select a track", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1,padx=120)
Label(master, text="Volume", font =("Calibri",12),fg="red").grid(sticky="N", row=4)
song_title =Label(master, font =("Calibri",12))
song_title.grid(sticky="N", row =3);
volume_label =Label(master, font =("Calibri",12))
volume_label.grid(sticky="N", row =5);

#buttons 
Button(master, text="select song", font=("Calibri",12), command=select_track).grid(sticky="N", row=2)
Button(master, text="Resume", font=("Calibri",12)).grid(sticky="W", row=3)
Button(master, text="Pause", font=("Calibri",12)).grid(sticky="E", row=3)
Button(master, text="-", font=("Calibri",12),width=5).grid(sticky="W", row=5)
Button(master, text="+", font=("Calibri",12),width=5).grid(sticky="E", row=5)

master.mainloop()