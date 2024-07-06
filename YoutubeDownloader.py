"""

Author: AlonsoR04

"""

import tkinter
from tkinter import messagebox
from pytube import YouTube
from sys import argv
import os

def comprobarLink():
    """Checks link's format"""
    enlace = link.get()
    if enlace[:32] == "https://www.youtube.com/watch?v=":
        return True
    else:
        return False

    

def descargarVideo():
    """Downloads link as a MP4"""

    if comprobarLink() == False:
        messagebox.showinfo(title="Error", message="Make sure link follows this form: https://www.youtube.com/watch?v=#...#")

    else:
    
        messagebox.showinfo(title="Message", message="Your video is currently downloading. Check Downloads folder. ")
        
        enlace= link.get()
        yt = YouTube(enlace)

        yd = yt.streams.get_highest_resolution()

        user = os.environ["USERPROFILE"]
        print(user)
        yd.download(user+"/Downloads")

def descargarAudio():
    """Downloads link as a MP3"""

    if comprobarLink() == False:
        messagebox.showinfo(title="Error", message="Make sure link follows this form: https://www.youtube.com/watch?v=#...#")

    else:

        messagebox.showinfo(title="Message", message="Your audio is currently downloading. Check Downloads folder.")
        
        enlace= link.get()
        yt = YouTube(enlace)

        yd = yt.streams.get_audio_only()
        

        user = os.environ["USERPROFILE"]
        print(user)
        yd.download(user+"/Downloads")
        
# User Interface using TkInter

window = tkinter.Tk()
window.title("Youtube Video Downloader")
window.geometry("400x200")
window.config(background="#D1D4D6")

espacio = tkinter.Label(window,bg= "#D1D4D6")
espacio.pack()

label1 = tkinter.Label(window, text= "Link:", bg = "#99D2FE", fg= "#000000",width= 21, relief= "raised")
label1.pack()

espacio = tkinter.Label(window,bg= "#D1D4D6")
espacio.pack()

link = tkinter.Entry(window,bg="#FFFFFF",fg="blue",width= 25)
link.pack()

espacio = tkinter.Label(window,bg= "#D1D4D6")
espacio.pack()

button = tkinter.Button(window, text= "DOWNLOAD VIDEO", command= descargarVideo, activebackground= "#99D2FE",bg="#ABE399")
button.pack()

espacio = tkinter.Label(window,bg= "#D1D4D6")
espacio.pack()

button = tkinter.Button(window, text= "DOWNLOAD AUDIO", command= descargarAudio, activebackground= "#99D2FE",bg="#ABE399")
button.pack()


window.mainloop()

    
