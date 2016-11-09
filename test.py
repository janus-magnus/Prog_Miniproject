import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        print('1')
        self.root.mainloop()
        print('3')

    def update_clock(self):
        print('2')
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()