from tkinter import *
import API_controler
import threading
import time



class screenFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        Frame.display_label_1 = Label()
        Frame.display_label_2 = Label()
        Frame.display_label_3 = Label()
        Frame.display_label_4 = Label()
        Frame.display_label_5 = Label()
        self.update_tweets()
        Frame.display_label_1.pack()
        Frame.display_label_2.pack()
        Frame.display_label_3.pack()
        Frame.display_label_4.pack()
        Frame.display_label_5.pack()

    def update_loop(self):
        while True:
            self.update_tweets()
            print('hit')
            self.update()
            time.sleep(60) # 10 min

    def update_tweets(self):
        timeline = API_controler.get_latest_tweets()

        tweet_counter = 1
        for tweet in timeline:  # dit kan eleganter denk ik, maar ik heb op het moment geen betere oplossing
            text_to_set = tweet['text']
            if tweet_counter == 1:
                Frame.display_label_1['text'] = text_to_set
            if tweet_counter == 2:
                Frame.display_label_2['text'] = text_to_set
            if tweet_counter == 3:
                Frame.display_label_3['text'] = text_to_set
            if tweet_counter == 4:
                Frame.display_label_4['text'] = text_to_set
            if tweet_counter == 5:
                Frame.display_label_5['text'] = text_to_set
            if tweet_counter == 6:
                break
            tweet_counter += 1




sfTk = Tk()
sfTk.title('NS Tweetbot Screen')
sfTk.geometry('500x500')
sf = screenFrame(sfTk)

thread = threading.Thread(target=sf.update_loop())
thread.start()
sf.mainloop()

