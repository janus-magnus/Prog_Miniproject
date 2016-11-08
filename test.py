from tkinter import *
import API_controler
import threading
import time

display_text = ''

class screenFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        Frame.approveB = Button( text='Approve', command=self.approve)
        Frame.display_label = Label()


        Frame.display_label['text'] = 'test'
        Frame.display_label.grid(row=0, column=0)
        Frame.approveB.grid(row=0, column=1)




    def approve(self):
        Frame.display_label['text'] = 'ttesfrdhest'





sfTk = Tk()
sfTk.title('NS Tweetbot Screen')
sfTk.geometry('500x500')
sf = screenFrame(sfTk)
sf.mainloop()


