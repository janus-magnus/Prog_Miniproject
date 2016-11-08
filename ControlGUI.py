import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path
import API_controler
import csv
import datetime
from defenitions import popMessage


reject_file = Path('rejectedTweets.csv')

tweet_que_file = Path('tweet_que.txt')

if not tweet_que_file.is_file():
    print('dingdong')

try:
    with open('tweet_que.txt', 'r') as twt_que:
        global tweet_list
        tweet_list = []
        text = ""
        for line in twt_que:
            text += line
            #tweet_list.append(line.strip())
        tweet_list = text.split("||")
        print(tweet_list)
        if tweet_list[0] == "":
            popMessage("Er zijn geen tweets om te controleren.")
except FileNotFoundError:
    print('No tweets yet')


class controlFrame(Frame):
    def __init__(self, master=None):
        global tweet_list
        Frame.__init__(self, master)

        Frame.approveB = Button(self, text='Approve', command=self.approve)
        Frame.rejectB = Button(self,text='Reject', command=self.reject)
        Frame.control_textbox = Text(self, width=50, height=25)

        Frame.control_textbox.insert(END, tweet_list[0])
        Frame.control_textbox.configure(state='disabled')
        Frame.control_textbox.grid(row=0, column=0)
        Frame.approveB.grid(row=2, column=1)
        Frame.rejectB.grid(row=2, column=2)

        self.pack()

    def approve(self):
        global tweet_list
        API_controler.place_tweet(tweet_list[0])  # hier wordt de tweet geplaatst

        tweet_list.remove(tweet_list[0]) #haal de tweet uit de lijst
        self.update_que()
        Frame.control_textbox.configure(state='normal')
        Frame.control_textbox.delete(1.0, END)
        if tweet_list[0] == "": #check of de lijst met te controleren tweets leeg is
            popMessage("Er zijn geen tweets meer om te controleren.")
        else:
            Frame.control_textbox.insert(END, tweet_list[0])
            Frame.control_textbox.configure(state='disabled')
            lfTk.update()


    def reject(self):
        global tweet_list
        if not reject_file.is_file():
            rejects = open('rejectedTweets.csv', 'w')
            reject_writer = csv.writer(rejects, delimiter=';')
        else:
            rejects = open('rejectedTweets.csv', 'a')
            reject_writer = csv.writer(rejects, delimiter=';')

        tweet_to_reject = repr(tweet_list[0])
        tweet_to_reject = tweet_to_reject.strip("\'")
        log_time = datetime.datetime.now()
        reject_log = [tweet_to_reject,log_time]
        reject_writer.writerow(reject_log)

        tweet_list.remove(tweet_list[0])
        self.update_que()
        Frame.control_textbox.configure(state='normal')
        Frame.control_textbox.delete(1.0, END)
        if tweet_list[0] == "": #check of de lijst met te controleren tweets leeg is
            popMessage("Er zijn geen tweets meer om te controleren.")
        else:
            Frame.control_textbox.insert(END, tweet_list[0])
            Frame.control_textbox.configure(state='disabled')
            lfTk.update()


    def update_que(self):
        with open('tweet_que.txt','w') as twtq:
            for i in tweet_list:
                if i != "":
                    write_line = i + '\n'
                    twtq.write(write_line)

lfTk = Tk()
lfTk.title('NS Tweetbot')
lfTk.geometry('500x500')
lf = controlFrame(lfTk)
lf.mainloop()
