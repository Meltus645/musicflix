#libs 
import os
from pygame import mixer
from tkinter import  Tk, Frame, LabelFrame, GROOVE,Label, Button, filedialog,PhotoImage
import pickle

play_volume =float(0.5)

# commands
def select_track():
	filename =filedialog.askopenfilename(initialdir="C:/", title ="Please select a song")
	selected_track =filename
	track_title =filename.split("/")
	track_title =track_title[-1]

	try:
		mixer.init()
		mixer.music.load(selected_track)
		mixer.music.set_volume(play_volume)
		mixer.music.play()
		song_title.config(fg="green", text=str(track_title))
		volume_label.config(fg="green", text=str(play_volume))
	except Exception as e:
		print(e)
		song_title.config(fg="red", text="Error, playing track")
		pass

def volume_down():
	try:
		global play_volume
		if play_volume <=0:
			volume_label.config(font=("Calibri",12), fg="grey", text="Muted")
			return
		play_volume =play_volume -float(0.1)
		play_volume =round(play_volume,1)
		mixer.music.set_volume(play_volume)
		volume_label.config(font=("Calibri",12), fg="green", text=str(play_volume))
	except Exception as e:
		song_title.config(fg="red", text="No track selected")
		print(e)

def volume_up():
	try:
		global play_volume
		if play_volume >=1:
			volume_label.config(font=("Calibri",12), fg="red", text="Max")
			return
		play_volume =play_volume +float(0.1)
		play_volume =round(play_volume,1)
		mixer.music.set_volume(play_volume)
		volume_label.config(font=("Calibri",12), fg="green", text=str(play_volume))
	except Exception as e:
		song_title.config(fg="red", text="No track selected")
		print(e)
def pause():
	try:
		mixer.music.pause()
	except Exception as e:
		print(e)
		song_title.config(fg="red", text="No track selected")
def resume():
	try:
		mixer.music.unpause()
	except Exception as e:
		print(e)
		song_title.config(fg="red", text="No track selected")
# screen 
root =Tk()
root.geometry("600x400")
root.title("Musiflix Player")

class Player(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.master =master
		self.pack()
		self.playlist =[]
		self.model_frame()
	def model_frame(self):
		self.track =LabelFrame(self,
				text="Track Hits",
				font =("times new roman",15,"bold"),
				bg ="dodgerblue",
				fg ="white",
				relief =GROOVE
			)
		self.track.configure(
				width =410,
				height =300
			)
		self.track.grid(row=0, column=0)

		self.tracklist =LabelFrame(self,
				text=f"Playlist  {len(self.playlist)}",
				font =("times new roman",15,"bold"),
				bg ="red",
				fg ="white",
				relief =GROOVE
			)
		self.tracklist.configure(
				width =190,
				height =400
			)
		self.tracklist.grid(row=0, column=1,rowspan=3)

		self.controls =LabelFrame(self,
				font =("times new roman",15,"bold"),
				bg ="white",
				fg ="white",
				relief =GROOVE
			)
		self.controls.configure(
				width =410,
				height =100
			)
		self.controls.grid(row=1, column=0,pady=5,padx=10)
#labels
"""
Label(master, text="Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0,padx=120)
Label(master, text="Please select a track", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1,padx=120)
Label(master, text="Volume", font =("Calibri",12),fg="red").grid(sticky="N", row=4)
song_title =Label(master, font =("Calibri",12))
song_title.grid(sticky="N", row =3);
volume_label =Label(master, font =("Calibri",12))
volume_label.grid(sticky="N", row =5);

#buttons 
Button(master, text="select song", font=("Calibri",12), command=select_track).grid(sticky="N", row=2)
Button(master, text="Resume", font=("Calibri",12),command =resume).grid(sticky="W", row=3)
Button(master, text="Pause", font=("Calibri",12),command =pause).grid(sticky="E", row=3)
Button(master, text="-", font=("Calibri",12),width=5,command=volume_down).grid(sticky="W", row=5)
Button(master, text="+", font=("Calibri",12),width=5,command=volume_up).grid(sticky="E", row=5)
"""
player =Player(master=root)
root.mainloop()