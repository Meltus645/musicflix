from pygame import mixer
from tkinter import  Tk, Label, Button, filedialog

# screen 

master =Tk()
master.title("Musiflix Player")

Label(master, text="Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0,padx=120)
Label(master, text="Select track", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1,padx=120)
master.mainloop()