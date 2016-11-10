import tkinter as tk
from tkinter import ttk

def popMessage(msg):
    '''maakt een popup window aan
    >>> popMessage('test msg')
    '''
    popup = tk.Tk()
    popup.wm_title("Tweet info")
    label = ttk.Label(popup, text=msg)
    label.pack()
    button = ttk.Button(popup, text="Ok!", command = popup.destroy)
    button.pack()
    popup.mainloop()

#import doctest
#doctest.testmod()