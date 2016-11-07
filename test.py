from twython import Twython

API_key = 'r44TpHBZ5ycKGiaSKDGkcBDEP'  # App API key
API_key_secret = 'r8oMp8hPdtZsezXKYvwgH4Xf5XD2MneflJzpJfiBsQAz9rQNXc' # secret key moet eigenlijk niet leesbaar zijn hier
OAuth_TK = '795684707501539330-B5vblQn2f2ELJLeQxcRm1Ta8bdCb45e'  # O Auth token
OAuth_TK_secret = 'Uw6ePHCuttGXvFP1FPHqeTTg4cC3JDRP1POUlqZaWu2Hn'  # O auth token secret moet eigenlijk niet leesbaar zijn hier

T = Twython(API_key, API_key_secret,OAuth_TK ,OAuth_TK_secret)

T.update_status(status='Test')  # hier wordt de tweet geplaats, moet nog worden beveiligdt met een charlimit van 140