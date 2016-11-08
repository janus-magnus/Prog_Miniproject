from tkinter import *
import API_controler
import threading
import time

display_text = ''

class screenFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        global display_label
        Frame.display_label = Label(text=API_controler.get_latest_tweet())
        Frame.display_label.pack()





sfTk = Tk()
sfTk.title('NS Tweetbot Screen')
sfTk.geometry('500x500')
sf = screenFrame(sfTk)
sf.mainloop()


