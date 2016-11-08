from tkinter import *
import API_controler
import threading
import time



class screenFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        Frame.display_label = Label()
        Frame.display_label['text'] = API_controler.get_latest_tweet()
        Frame.display_label.pack()





    def update_loop(self):
        while True:
            self.update_tweet()
            time.sleep(60) # 10 min

    def update_tweet(self):
        text_to_set = API_controler.get_latest_tweet()
        Frame.display_label['text'] =text_to_set




sfTk = Tk()
sfTk.title('NS Tweetbot Screen')
sfTk.geometry('500x500')
sf = screenFrame(sfTk)
sf.mainloop()
thread = threading.Thread(target=sf.update_loop())
thread.daemon = True
thread.start()

