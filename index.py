#libs 
import os
from pygame import mixer
from tkinter import  Tk, Frame,END, LabelFrame, GROOVE,Label,SINGLE, Button, filedialog,PhotoImage,DoubleVar,Listbox, Scale, HORIZONTAL,VERTICAL, Scrollbar
import pickle

play_volume =float(0.5)

# commands

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
		if os.path.exists("tracks.pickle"):
			with open ("tracks.pickle", "r") as f:
				self.playlist =pickle.load(f)
		else:
			self.playlist =[]

		# player state flags
		self.track_index =0
		self.track_paused =True
		self.track_played =False

		self.model_frame()
		self.track_widget()
		self.tracklist_widget()
		self.controls_widget()
	# frames
	def model_frame(self):
		self.track =LabelFrame(self,
				relief =GROOVE
			)
		self.track.configure(
				width =410,
				height =300
			)
		self.track.grid(row=0, column=0,pady=10,padx=10)

		self.tracklist =LabelFrame(self,
				relief =GROOVE
			)
		self.tracklist.configure(
				width =190,
				height =420
			)
		self.tracklist.grid(row=0, column=1,rowspan=3,pady=10,padx=10)

		self.controls =LabelFrame(self,
				font =("times new roman",15,"bold"),
				bg ="white",
				fg ="white",
				bd =0,
				relief =GROOVE
			)
		self.controls.configure(
				width =410,
				height =100
			)
		self.controls.grid(row=1, column=0,pady=10,padx=10)

	# widgets
	def track_widget(self):
		self.canvas =Label(self.track,font =("times new roman",15,"bold"),bg="white", fg ="dodgerblue")
		self.canvas['text'] ="Hit tracks"; 
		self.canvas.configure(width =33, height =1)
		self.canvas.grid(row =0,column =0)

		self.canvas =Label(self.track,image=track_ico) 
		self.canvas.configure(width =300, height =240)
		self.canvas.grid(row =1,column =0)

		self.canvas =Label(self.track,font =("Calibri",13),bg="white", fg ="dodgerblue")
		self.canvas['text'] ="Musicflix Player"; 
		self.canvas.configure(width =44, height =1)
		self.canvas.grid(row =2,column =0)

	def tracklist_widget(self):
		self.listtitle =Label(self.tracklist,font =("times new roman",15,"bold"),bg="white", fg ="dodgerblue")
		self.listtitle['text'] =f"Playlist:  {len(self.playlist)} "
		self.listtitle.configure(width =10, height =1)
		self.listtitle.grid(row =0,column =0)

		self.scrollbar =Scrollbar(self.tracklist,orient =VERTICAL)
		self.scrollbar.grid(row=0, column=1,rowspan =10, sticky="NS")

		self.list =Listbox(self.tracklist, selectmode =SINGLE,
			yscrollcommand =self.scrollbar.set, selectbackground ="sky blue")
		self.track_listing()
		self.list.config(height =22)
		self.scrollbar.config(command =self.list.yview)
		self.list.grid(row=2, column=0, rowspan =5)

	def track_listing(self):
		for index, track in enumerate(self.playlist):
			self.list.insert(index,os.path.basename(track))

	def controls_widget(self):
		self.tracklister =Button(self.controls, 
			font =("times new roman",15,"bold"),
			bg="white", fg ="dodgerblue", padx =10,pady =5,
			command =self.select_track
			)
		self.tracklister['text'] ="Load tracks"
		self.tracklister.grid(row =0,column =0,padx=10,pady =5)

		self.prevbutton =Button(self.controls,image =prev_icon)
		self.prevbutton.grid(row =0,column =1,pady =5)

		self.pausebutton =Button(self.controls,image =playicon)
		self.pausebutton.grid(row =0,column =2,pady =5)

		self.nextbutton =Button(self.controls,image =next_icon)
		self.nextbutton.grid(row =0,column =3,pady =5)

		self.volume =DoubleVar()
		self.slider =Scale(self.controls, from_ =0, to =10, orient =HORIZONTAL)
		self.slider['variable'] =self.volume
		self.slider['command'] =self.change_volume
		self.slider.set(3)
		self.slider.grid(row =0, column=4,padx=10,pady =5)

	def change_volume(self, event =None):
		self.v =self.volume.get()


	def select_track(self):
		self.tunes =[]
		directory =filedialog.askdirectory()

		for rooot, dirs, files in os.walk(directory):
			for file in files:
				if os.path.splitext(file)[1] =='.mp3':
					path =(rooot + '/' + file).replace('\\','/')
					self.tunes.append(path)
		with open("tracks.pickle", "wb") as f:
			pickle.dump(self.tunes, f) 
		self.playlist =self.tunes
		self.listtitle['text'] =f"Playlist:  {len(self.playlist)}"
		self.list.delete(0, END)
		self.track_listing()
		"""
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
			"""

#images
track_ico =PhotoImage(file ="ico/headsets.gif")
prev_icon =PhotoImage(file ="ico/prev.gif")
pauseicon =PhotoImage(file ="ico/pause.gif")
playicon =PhotoImage(file ="ico/play.gif")
next_icon =PhotoImage(file ="ico/next.gif")

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