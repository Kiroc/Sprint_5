import random
import string

URL_main='https://stellarburgers.nomoreparties.site/'
URL_reg='https://stellarburgers.nomoreparties.site/register'
URL_auth = 'https://stellarburgers.nomoreparties.site/login'
URL_profile = 'https://stellarburgers.nomoreparties.site/account/profile'
URL_recover='https://stellarburgers.nomoreparties.site/forgot-password'

class Reg:
    user_name = f'Kirill'
    email = f'kirill_sosnitskiy_17_123@yandex.ru'
    password = f'12345678'

class RandomUser:
    user_name =''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email+='@ya.ru'
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


