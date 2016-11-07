import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path

file = Path('tweetQue.txt')


class loginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        Frame.submitB = Button(self, text='Submit', command=self.submit)
        Frame.input_textbox = Text(self, width=50, height=25)

        Frame.input_textbox.grid(row=0,column=0)
        Frame.submitB.grid(row=1, column=1)


        self.pack()

    def submit(self):
        text = Frame.input_textbox.get('1.0',END)
        #hij telt enters en alle andere tekens ook gewoon mee nog.
        if len(text) < 4:
            popMessage("Tweet moet minimaal 4 tekens lang zijn!.")
        elif len(text) < 140:
            if not file.is_file() :
                tweetFile = open('TweetQue.txt', 'w')
            else:
                tweetFile = open('TweetQue.txt', 'a')

            tweetFile.write(text)
            popMessage("Tweet is verzonden en wacht op goedkeuring.")
            tweetFile.close()
        else:
            popMessage("Tweet mag maximaal 140 karakters bevatten!.")


def popMessage(msg):
    popup = tk.Tk()
    popup.wm_title("Tweet info")
    label = ttk.Label(popup, text=msg)
    label.pack()
    button = ttk.Button(popup, text="Ok!", command = popup.destroy)
    button.pack()
    popup.mainloop()

lfTk = Tk()
lfTk.title('NS Tweetbot')
lfTk.geometry('500x500')
lf = loginFrame(lfTk)
lf.mainloop()
