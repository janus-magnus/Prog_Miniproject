from twython import Twython
from pyowm import *

T_API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # Twitter App API key
T_API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # twitter secret key
T_OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
T_OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret
W_API_key = '0292ef38878076e5a546762d1c2a5ff8'  # weather API key

owmAPI = OWM(W_API_key)
T = Twython(T_API_key, T_API_key_secret,T_OAuth_TK ,T_OAuth_TK_secret)

def place_tweet(status):
    '''plaatst een tweet met de mee gegeven status als inhoud'''
    T.update_status(status=status)

def weather():
    '''haalt de weer gegevens op van openweathermap en return weather_ob'''
    owm = owmAPI.weather_at_place('Utrecht,NL')
    weather_ob = owm.get_weather()
    return weather_ob

def get_latest_tweets():
    '''haalt de timeline van twitter en return timeline'''
    timeline = T.get_user_timeline()
    return timeline

