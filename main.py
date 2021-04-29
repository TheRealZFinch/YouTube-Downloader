from pytube import YouTube
from tkinter import *

root = Tk()

def Download():
  video = YouTube('https://www.youtube.com/watch?v=' + str(urlInput.get()))
  video = video.streams.get_lowest_resolution()
  video.download()

urlInput = Entry(root)
urlInput.grid(row=0, column=0)

dwlButton = Button(root, text="Download", pady="25", padx="50", command=Download)
dwlButton.grid(row=0, column=1)


root.mainloop()