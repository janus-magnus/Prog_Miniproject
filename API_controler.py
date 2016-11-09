from twython import Twython
from pyowm import *


# Twittwer API Stuff
T_API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # Twitter App API key
T_API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # secret key moet eigenlijk niet leesbaar zijn hier
T_OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
T_OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret moet eigenlijk niet leesbaar zijn hier
# weather API
W_API_key = '0292ef38878076e5a546762d1c2a5ff8'  # weather API key

owmAPI = OWM(W_API_key)
T = Twython(T_API_key, T_API_key_secret,T_OAuth_TK ,T_OAuth_TK_secret)


def place_tweet(status):
    T.update_status(status=status)

def weather():
    owm = owmAPI.weather_at_place('Utrecht,NL')
    weather_ob = owm.get_weather()
    clouds = weather_ob.get_clouds()  # Get cloud coverage
    rain = weather_ob.get_rain()  # Get rain volume
    wind = weather_ob.get_wind()  # Get wind degree and speed
    humidity = weather_ob.get_humidity()  # Get humidity percentage
    prs = weather_ob.get_pressure()  # Get atmospheric pressure
    temp = weather_ob.get_temperature(unit='celsius')
    status = weather_ob.get_detailed_status()  # Get detailed weather status

def get_latest_tweets():
    timeline = T.get_user_timeline()

    return timeline

