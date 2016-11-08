import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path
import API_controler
import csv
import datetime


reject_file = Path('rejectedTweets.csv')

tweet_que_file = Path('tweet_que.txt')

if not tweet_que_file.is_file():
    print('dingdong')

try:
    with open('tweet_que.txt', 'r') as twt_que:
        global tweet_list
        tweet_list = []
        for line in twt_que:
            tweet_list.append(line.strip())
        print(tweet_list)
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

        tweet_list.remove(tweet_list[0])
        Frame.control_textbox.configure(state='normal')
        Frame.control_textbox.delete(1.0, END)
        Frame.control_textbox.insert(END, tweet_list[0])  # er moet hier een guard komen die controleert of de tweet_list niet leeg is
        Frame.control_textbox.configure(state='disabled')
        lfTk.update()
        self.update_que()

    def reject(self):
        global tweet_list
        if not reject_file.is_file():
            rejects = open('rejectedTweets.csv', 'w')
            reject_writer = csv.writer(rejects, delimiter=';')
        else:
            rejects = open('rejectedTweets.csv', 'a')
            reject_writer = csv.writer(rejects, delimiter=';')

        tweet_to_reject = tweet_list[0]
        log_time = datetime.datetime.now()
        reject_log = [tweet_to_reject,log_time]
        reject_writer.writerow(reject_log)

        tweet_list.remove(tweet_list[0])
        Frame.control_textbox.configure(state='normal')
        Frame.control_textbox.delete(1.0, END)
        Frame.control_textbox.insert(END, tweet_list[0])  # er moet hier een guard komen die controleert of de tweet_list niet leeg is
        Frame.control_textbox.configure(state='disabled')

        lfTk.update()
        self.update_que()

    def update_que(self):
        with open('tweet_que.txt','w') as twtq:
            for i in tweet_list:
                write_line = i + '\n'
                twtq.write(write_line)

lfTk = Tk()
lfTk.title('NS Tweetbot')
lfTk.geometry('500x500')
lf = controlFrame(lfTk)
lf.mainloop()
