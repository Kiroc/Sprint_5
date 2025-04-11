import random
import string

URL_main='https://stellarburgers.nomoreparties.site/'
URL_reg=URL_main+'register'
URL_auth = URL_main+'login'
URL_profile = URL_main+'account/profile'
URL_recover=URL_main+'forgot-password'

class Reg:
    user_name = f'Kirill'
    email = f'kirill_sosnitskiy_17_123@yandex.ru'
    password = f'12345678'

class RandomUser:
    user_name =''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email+='@ya.ru'
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


