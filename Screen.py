from tkinter import *
import API_controler

class ScreenFrame():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('NS Tweetbot Screen')
        self.display_label_1 = Label()
        self.display_label_2 = Label()
        self.display_label_3 = Label()
        self.display_label_4 = Label()
        self.display_label_5 = Label()

        self.display_label_1.pack()
        self.display_label_2.pack()
        self.display_label_3.pack()
        self.display_label_4.pack()
        self.display_label_5.pack()

        self.update_tweets()
        self.root.mainloop()

    def update_tweets(self):
        timeline = API_controler.get_latest_tweets()

        tweet_counter = 1
        for tweet in timeline:  # dit kan eleganter denk ik, maar ik heb op het moment geen betere oplossing
            text_to_set = tweet['text']
            if tweet_counter == 1:
                self.display_label_1['text'] = text_to_set
            if tweet_counter == 2:
                self.display_label_2['text'] = text_to_set
            if tweet_counter == 3:
                self.display_label_3['text'] = text_to_set
            if tweet_counter == 4:
                self.display_label_4['text'] = text_to_set
            if tweet_counter == 5:
                self.display_label_5['text'] = text_to_set
            if tweet_counter == 6:
                break
            tweet_counter += 1
            print('here here')
        self.root.after(60000, self.update_tweets)

sf = ScreenFrame()
