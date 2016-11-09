from tkinter import *
import API_controler

class ScreenFrame():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x510')
        self.root.title('NS Tweetbot Screen')

        #Voeg een label aan de bovenkant van het scherm toe.
        self.display_label = Label(text='Laatste 5 tweets van andere gebruikers.',
                                   fg='white',bg='#163c76', width=55, height=2,bd=1, relief=GROOVE, font='bold')
        self.display_label.pack()

        self.get_weather()

        self.update_tweets()
        self.root.mainloop()

    def update_tweets(self): #zet de laatste tweets in het scherm
        timeline = API_controler.get_latest_tweets()

        tweet_counter = 1
        for tweet in timeline:
            text_to_set = tweet['text']
            if tweet_counter == 6:
                break
            #zet de tekst van de tweet in de label, en er wordt opmaak toegevoegd aan de label.
            self.display_label = Label(text=text_to_set,wraplength='500', fg='#163c76',bg='white',
                                       width=55, height=5,bd=1, relief=GROOVE, font='bold')
            self.display_label.pack()
            tweet_counter += 1

        #update het scherm elke 10minuten(tijd staat in miliseconden)
        self.root.after(600000, self.update_tweets)

    def get_weather(self):  # placeholder moet uitgebreid worden met auto update etc.
        weather_ob = API_controler.weather()  # weer object

       # dit zijn de functies die op de het weather_ob kan uitvoeren

        clouds = weather_ob.get_clouds()  # Get cloud coverage
        rain = weather_ob.get_rain()  # Get rain volume
        wind = weather_ob.get_wind()  # Get wind degree and speed/ in een dict
        humidity = weather_ob.get_humidity()  # Get humidity percentage
        temp = weather_ob.get_temperature(unit='celsius')
        status = weather_ob.get_detailed_status()  # Get detailed weather status

        print(temp, clouds, humidity, rain)  # voorbeeld

sf = ScreenFrame()
