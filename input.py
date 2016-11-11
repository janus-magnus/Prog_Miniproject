import tkinter as tk
from pathlib import Path
from Defenitions import popMessage

file = Path('tweet_que.txt')

class InputApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        #set configures voor de grid zodat deze intact blijft
        self.columnconfigure(0, weight=3)
        self.rowconfigure(0,weight=3)
        self.rowconfigure(1,weight=3)
        #maak textbox
        self.input_textbox = tk.Text(self, width=50, height=15)
        self.input_textbox.grid(row=0, sticky='WE')
        #maak Button
        self.submitB = tk.Button(self, text='Verstuur tweet', command=self.submit, bg='#0079D3', fg='white')
        self.submitB.grid(row=1, sticky='WE')
        self.pack()

    def submit(self):
        '''de ingevoerde text wordt wegeschreven naar tweet_que.txt en input_text box wordt leeg gemaakt'''
        text = self.input_textbox.get('1.0',tk.END)
        #zorg dat ingevoerde tweet minstens 4 tekens lang is
        if len(text) < 4:
            popMessage("Tweet moet minimaal 4 tekens lang zijn!.")
        #bericht mag niet langer zijn dan 140 charcters
        elif len(text) <= 140:
            #check of file bestaat
            if not file.is_file() :
                tweetFile = open('tweet_que.txt', 'w')
            else:
                tweetFile = open('tweet_que.txt', 'a')
            text = text + "||"
            #schrijf de tweet naar het bestand
            tweetFile.write(text)
            tweetFile.close()
            #verwijder de tweet uit het scherm zodat een volgende gebruiker een leeg scherm heeft
            self.input_textbox.delete('1.0', tk.END)
            self.update()
            popMessage("Tweet is verzonden en wacht op goedkeuring.")
        else:
            popMessage("Tweet mag maximaal 140 karakters bevatten!.")

if __name__ == '__main__':
    root = tk.Tk()
    InputApp(root).pack
    root.title('NS Tweetbot Input')
    root.geometry('500x300')
    root.configure(bg='#FFC917')
    root.mainloop()

