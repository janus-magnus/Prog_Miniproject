from tkinter import *
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

        if not file.is_file() :
            tweetFile = open('TweetQue.txt', 'w')
        else:
            tweetFile = open('TweetQue.txt', 'a')

        tweetFile.write(text)
        tweetFile.close()



lfTk = Tk()
lfTk.title('NS Tweetbot')
lfTk.geometry('500x500')
lf = loginFrame(lfTk)
lf.mainloop()