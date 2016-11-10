import tkinter as tk
from pathlib import Path
from Defenitions import popMessage

file = Path('tweet_que.txt')

class InputApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.input_textbox = tk.Text(self, width=50, height=25)
        self.submitB = tk.Button(self, text='Submit', command=self.submit)
        self.input_textbox.grid(row=0,column=0)
        self.submitB.grid(row=1, column=1)
        self.pack()

    def submit(self):
        text = self.input_textbox.get('1.0',tk.END)
        #hij telt enters en alle andere tekens ook gewoon mee nog.
        if len(text) < 4:
            popMessage("Tweet moet minimaal 4 tekens lang zijn!.")
        elif len(text) < 140:
            if not file.is_file() :
                tweetFile = open('tweet_que.txt', 'w')
            else:
                tweetFile = open('tweet_que.txt', 'a')
            text = text + "||"
            tweetFile.write(text)
            tweetFile.close()
            self.input_textbox.delete('1.0', tk.END)
            self.update()
            popMessage("Tweet is verzonden en wacht op goedkeuring.")
        else:
            popMessage("Tweet mag maximaal 140 karakters bevatten!.")

if __name__ == '__main__':
    root = tk.Tk()
    InputApp(root).pack
    root.title('NS Tweetbot Input')
    root.geometry('500x500')
    root.mainloop()

