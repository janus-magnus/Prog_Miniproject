from tkinter import *
import API_Controler as ap
from datetime import datetime

last_tweet = ""
show_weather = 0

class ScreenFrame():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('510x510')
        self.root.title('NS Tweetbot Screen')
        self.root.columnconfigure(0, weight=3)
        self.root.rowconfigure(0,minsize=40,weight=3)
        #Voeg een label aan de bovenkant van het scherm toe.
        self.display_label_top = Label(text='Laatste 5 tweets van andere gebruikers.',
                                   fg='white',bg='#163c76',bd=1, relief=GROOVE, font='bold')
        self.display_label_top.grid(row=0,columnspan=2, sticky=W+E+N+S)

        self.update_tweets()

        self.root.mainloop()

    def update_tweets(self): #zet de laatste 5 tweets in het scherm
        '''haalt de laats 5 tweets op en update labels er mee. als er voor een tijd geen nieuw tweets zijn
        wordt er na er weergegevens wergegeven'''
        global last_tweet, show_weather
        #roep de API aan
        timeline = ap.get_latest_tweets()

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
            self.root.rowconfigure(tweet_counter,minsize=94,weight=3)
            self.display_label = Label(text=text_to_set,wraplength='450', fg='#163c76',bg='white',
                                       bd=1, relief=GROOVE, font='bold')
            self.display_label.grid(row=tweet_counter,columnspan=2, sticky=W+E+N+S)
            tweet_counter += 1

        #update het scherm elke 5minuten(tijd staat in miliseconden)
        self.root.after(300000, self.delete_tweets) #delete eerst de tweets
        self.root.after(300000, self.update_tweets) #zet dan de nieuwe tweets er weer in

    def delete_tweets(self):
        '''maakt het scherm leeg'''
        self.display_label.grid_remove()
        if show_weather == 1:
            self.weather_label.grid_remove()

    def get_weather(self):
        '''haalt de weer informatie op en zet het in labels voor weergave'''
        weather_ob = ap.weather() #roep het weer API aan

       # dit zijn de functies die op de het weather_ob kan uitvoeren
        wind = weather_ob.get_wind()  # haalt windgegevens op
        humidity = weather_ob.get_humidity()  # haalt luchtvochtingheid op
        temp = weather_ob.get_temperature(unit='celsius') # haalt de temp op
        status = weather_ob.get_status() # haalt weer op e.g. rain, sun, cloudy

        #de tijd van laatste update omzetten naar gewenste notatie
        text_date = datetime.strftime(weather_ob.get_reference_time(timeformat='date'), "%a %e %b om %H:%M:%S")

        #Voeg de labels van het weerbericht toe met de info.
        self.weather_label = Label(text="Het weer in Utrecht\n"+text_date, fg='#163c76',bg='#EEEEEE',
                                       bd=1, font=('normal', '14'))
        self.weather_label.grid(row=4, columnspan=2, sticky=E+W+N+S)

        self.weather_label = Label(text=status+"\t\t\tLuchtvochtigheid: "+str(humidity)+"%\nTemperatuur: "+str(temp['temp'])+"°C\tWindsnelheid: "+str(wind['speed'])+"km/u"
                                   ,anchor='n',fg='#163c76',bg='#EEEEEE',bd=1, font=('normal', '13'))
        self.weather_label.grid(row=5, columnspan=2, sticky=E+W+N+S)
sf = ScreenFrame()
