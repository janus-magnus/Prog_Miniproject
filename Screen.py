from tkinter import *
import API_controler
from datetime import datetime

last_tweet = ""
show_weather = 0

class ScreenFrame():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('490x510')
        self.root.title('NS Tweetbot Screen')

        #Voeg een label aan de bovenkant van het scherm toe.
        self.display_label_top = Label(text='Laatste 5 tweets van andere gebruikers.',
                                   fg='white',bg='#163c76', width=54, height=2,bd=1, relief=GROOVE, font='bold')
        self.display_label_top.grid(row=1)

        self.update_tweets()

        self.root.mainloop()

    def update_tweets(self): #zet de laatste 5 tweets in het scherm
        global last_tweet, show_weather
        #roep de API aan
        timeline = API_controler.get_latest_tweets()

        tweet_counter = 1
        for tweet in timeline:
            #zet de tekst van de tweet in 'text_to_set'
            text_to_set = tweet['text']

            if tweet_counter == 1: #zet de laatst geplaatste tweet vast
                if last_tweet == text_to_set:
                    show_weather = 1
                else:
                    last_tweet = text_to_set
                    show_weather = 0
            if tweet_counter == 6:
                if show_weather == 1:
                    self.get_weather()
                break

            #zet de tekst van de tweet in de label, en er wordt opmaak toegevoegd aan de label.
            self.display_label = Label(text=text_to_set,wraplength='490', fg='#163c76',bg='white',
                                       width=54, height=5,bd=1, relief=GROOVE, font='bold')
            self.display_label.grid(row=tweet_counter+1)
            tweet_counter += 1

        #update het scherm elke 10minuten(tijd staat in miliseconden)
        self.root.after(10000, self.delete_tweets) #delete eerst de tweets
        self.root.after(10000, self.update_tweets) #zet dan de nieuwe tweets er weer in

    def delete_tweets(self):
        self.display_label.grid_remove()
        if show_weather == 1:
            self.weather_label.grid_remove()

    def get_weather(self):#Zet het weer op het scherm
        weather_ob = API_controler.weather() #roep het weer API aan

       # dit zijn de functies die op de het weather_ob kan uitvoeren
        wind = weather_ob.get_wind()  # Get wind degree and speed/ in een dict
        humidity = weather_ob.get_humidity()  # Get humidity percentage
        temp = weather_ob.get_temperature(unit='celsius') # Get degrees in Celsius
        status = weather_ob.get_status() # Get weather status

        #de tijd van laatste update omzetten naar gewenste notatie
        text_date = datetime.strftime(weather_ob.get_reference_time(timeformat='date'), "%a %e %b om %H:%M:%S")

        #Voeg de labels van het weerbericht toe met de info.
        self.weather_label = Label(text="Het weer in Utrecht\n"+text_date, fg='#163c76',bg='#EEEEEE',
                                       width=44, height=4,bd=1, font=('normal', '14'))
        self.weather_label.grid(row=5)

        self.weather_label = Label(text=status+"\nLuchtvochtigheid: "+str(humidity)+"%"
                                            ,anchor="n",fg='#163c76',bg='#EEEEEE',width=27, height=5, bd=1, font=('normal', '13'))
        self.weather_label.grid(row=6, sticky=W)
        self.weather_label = Label(text="Temperatuur: "+str(temp['temp'])+"°C\nWindsnelheid: "+str(wind['speed'])+"km/u"
                                            ,anchor="n",fg='#163c76',bg='#EEEEEE',width=27, height=5, bd=1, font=('normal', '13'))
        self.weather_label.grid(row=6, sticky=E)

sf = ScreenFrame()
