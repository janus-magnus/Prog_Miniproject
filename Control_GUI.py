import tkinter as tk
from pathlib import Path
import API_Controler
import csv
import datetime
from Defenitions import popMessage

reject_file = Path('rejected_tweets.csv')
tweet_que_file = Path('tweet_que.txt')

def read_in():
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
    except FileNotFoundError:
        print('No tweets yet')

class ControlApp(tk.Frame):
    def __init__(self, master=None):
        global tweet_list
        tk.Frame.__init__(self, master)
        self.master = master
        self.approveB = tk.Button(self, text='Approve', command=self.approve)
        self.rejectB = tk.Button(self,text='Reject', command=self.reject)
        self.control_textbox = tk.Text(self, width=50, height=25)
        self.control_textbox.insert(tk.END, tweet_list[0])
        self.control_textbox.configure(state='disabled')
        self.control_textbox.grid(row=0, column=0)
        self.approveB.grid(row=2, column=1)
        self.rejectB.grid(row=2, column=2)
        self.pack()

    def approve(self):
        global tweet_list
        try:
            if tweet_list[0] is not None:
                API_Controler.place_tweet(tweet_list[0])  # hier wordt de tweet geplaatst
                tweet_list.remove(tweet_list[0]) #haal de tweet uit de lijst
                self.update_que()
                self.control_textbox.configure(state='normal')
                self.control_textbox.delete(1.0, tk.END)
                self.control_textbox.insert(tk.END, tweet_list[0])
                self.control_textbox.configure(state='disabled')
                self.update()
            else:
                raise IndexError
        except IndexError:
            popMessage("Er zijn geen tweets meer om te controleren.")


    def reject(self):
        global tweet_list
        try:
            if not reject_file.is_file():
                rejects = open('rejected_tweets.csv', 'w')
                reject_writer = csv.writer(rejects, delimiter=';')
            else:
                rejects = open('rejected_tweets.csv', 'a')
                reject_writer = csv.writer(rejects, delimiter=';')

            tweet_to_reject = repr(tweet_list[0])
            tweet_to_reject = tweet_to_reject.strip("\'")
            log_time = datetime.datetime.now()
            reject_log = [tweet_to_reject,log_time]
            reject_writer.writerow(reject_log)
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
    root.geometry('500x500')
    root.mainloop()
