from twython import Twython
from pyowm import *
from django.core.cache import cache

# Twittwer API Stuff
T_API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # Twitter App API key
T_API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # secret key moet eigenlijk niet leesbaar zijn hier
T_OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
T_OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret moet eigenlijk niet leesbaar zijn hier
# weather API
W_API_key = '23cf4ba4eba9811dec72a34c4a61b422'  # App API key


T = Twython(T_API_key, T_API_key_secret,T_OAuth_TK ,T_OAuth_TK_secret)
owm = OWM()

def place_tweet(status):
    T.update_status(status=status)

def weather():
    testw =  owm.weather_at_place('Utrecht,NL')
    print(testw)
    # werkt niet

def get_latest_tweets():
    timeline = T.get_user_timeline()

    return timeline

