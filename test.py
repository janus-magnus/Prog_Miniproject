from tkinter import *
import API_controler
import threading
import time

display_text = ''

class screenFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        global display_label
        Frame.display_label = Label(text='test')
        Frame.display_label.pack()
        Frame.testb = Button(text='test')
        Frame.testb.pack()
        self.pack()

    def test(self):
        Frame.di




sfTk = Tk()
sfTk.title('NS Tweetbot Screen')
sfTk.geometry('500x500')
sf = screenFrame(sfTk)
sf.mainloop()


