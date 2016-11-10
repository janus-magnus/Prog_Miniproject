import tkinter as tk
from pathlib import Path
from API_Controler import *
import csv
import datetime
from Defenitions import popMessage
from twython import exceptions as te

reject_file = Path('rejected_tweets.csv')
tweet_que_file = Path('tweet_que.txt')


def read_in():
    '''haalt de gegevens uit tweet_que.txt en slaat ze op in een list'''
    try:
        with open('tweet_que.txt', 'r') as twt_que:
            global tweet_list
            tweet_list = []
            text = ""
            for line in twt_que:
                text += line
            tweet_list = text.split("||")
    except FileNotFoundError:
        popMessage('No tweets yet')

class ControlApp(tk.Frame):
    def __init__(self, master=None):
        global tweet_list
        tk.Frame.__init__(self, master)
        self.master = master
        self.rowconfigure(0,weight=3)

        #maak buttons
        self.approveB = tk.Button(self, text='Approve', command=self.approve, bg='#0079D3', fg='white')
        self.rejectB = tk.Button(self,text='Reject', command=self.reject, bg='#0079D3', fg='white')
        #maak textbox
        self.control_textbox = tk.Text(self, width=50, height=15)
        self.control_textbox.insert(tk.END, tweet_list[0])
        self.control_textbox.configure(state='disabled')
        #zet alles in grid
        self.control_textbox.grid(row=0, columnspan=2, sticky='nesw')
        self.approveB.grid(row=2, column=0, sticky='nesw')
        self.rejectB.grid(row=2, column=1, sticky='nesw')
        self.pack()

    def approve(self):
        '''plaats de goedgekeurde tweet via place_tweet() en plaats de volgende tweet in het venster'''
        global tweet_list

        try:
            if tweet_list[0] is not None:
                try:
                    place_tweet(tweet_list[0])  # hier wordt de tweet geplaatst
                    tweet_list.remove(tweet_list[0]) #haal de tweet uit de lijst
                    self.update_que()
                    self.control_textbox.configure(state='normal')
                    self.control_textbox.delete(1.0, tk.END)
                    self.control_textbox.insert(tk.END, tweet_list[0])
                    self.control_textbox.configure(state='disabled')
                    self.update()
                except te.TwythonError:  # duplicate tweet protectie
                    popMessage('De tweet mag niet gelijk zijn aan de vorige')

            else:
                raise IndexError
        except IndexError:
            popMessage("Er zijn geen tweets meer om te controleren.")



    def reject(self):
        '''logs de afgekeurde tweet in rejected_tweets.csv en plaats de volgende tweet in het venster'''
        global tweet_list
        try:
            if not reject_file.is_file():
                rejects = open('rejected_tweets.csv', 'w')
                reject_writer = csv.writer(rejects, delimiter=';')
            else:
                rejects = open('rejected_tweets.csv', 'a')
                reject_writer = csv.writer(rejects, delimiter=';')

            #Zet de rejected tweet in het logfile
            tweet_to_reject = repr(tweet_list[0])
            tweet_to_reject = tweet_to_reject.strip("\'")
            log_time = datetime.datetime.now()
            reject_log = [tweet_to_reject,log_time]
            reject_writer.writerow(reject_log)
            #verwijder de tweet uit de que
            tweet_list.remove(tweet_list[0])
            self.update_que()
            self.control_textbox.configure(state='normal')
            self.control_textbox.delete(1.0, tk.END)
            self.control_textbox.insert(tk.END, tweet_list[0])
            self.control_textbox.configure(state='disabled')
            self.update()
        except IndexError:
            popMessage("Er zijn geen tweets meer om te controleren.")


    def update_que(self):
        #update het que bestand
        with open('tweet_que.txt','w') as twtq:
            for i in tweet_list:
                if i != "":
                    write_line = i + '\n'
                    twtq.write(write_line)

if __name__ == '__main__':
    read_in()
    root = tk.Tk()
    ControlApp(root).pack
    root.title('NS Tweetbot Control')
    root.geometry('500x300')
    root.configure(bg='#FFC917')
    root.mainloop()
