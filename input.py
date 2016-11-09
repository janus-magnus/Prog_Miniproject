from tkinter import *
from pathlib import Path
from defenitions import popMessage

file = Path('tweet_que.txt')

class inputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Frame.input_textbox = Text(self, width=50, height=25)
        Frame.submitB = Button(self, text='Submit', command=self.submit)
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
                tweetFile = open('Tweet_que.txt', 'w')
            else:
                tweetFile = open('Tweet_que.txt', 'a')
            text = text + "||"
            tweetFile.write(text)
            popMessage("Tweet is verzonden en wacht op goedkeuring.")
            tweetFile.close()
        else:
            popMessage("Tweet mag maximaal 140 karakters bevatten!.")
        Frame.input_textbox.delete(1.0, END)  # werkt niet geen idee waarom
        lfTk.update()

lfTk = Tk()
lfTk.title('NS Tweetbot')
lfTk.geometry('500x500')
lf = inputFrame(lfTk)
lf.mainloop()
