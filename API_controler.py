from twython import Twython
# Twittwer API Stuff
T_API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # App API key
T_API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # secret key moet eigenlijk niet leesbaar zijn hier
T_OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
T_OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret moet eigenlijk niet leesbaar zijn hier
# weather API
W_API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # App API key
W_API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # secret key moet eigenlijk niet leesbaar zijn hier
W_OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
W_OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret moet eigenlijk niet leesbaar zijn hier

T = Twython(T_API_key, T_API_key_secret,T_OAuth_TK ,T_OAuth_TK_secret)

def place_tweet(status):
    T.update_status(status=status)

def weather():
    # placeholder
