import requests
import string
from random import *
i = 0
i += 1

characters = string.ascii_letters + string.digits
password =  "".join(choice(characters) for x in range(randint(9, 9)))
email = string.digits
em =  "".join(choice(email) for x in range(randint(8, 8)))
ii = string.digits
id =  "".join(choice(ii) for x in range(randint(9, 12)))
while True:
    payload = {'miil': "077" + em , 'pw': password, 'log' : "FB", "playid" : id}
    url = 'https://midbuy.ru/PUBG/midasbuy/979712002/verification.php'#https://midbuy.ru/PUBG/midasbuy/here your telegram id/verification.php
    requests.post(url, data=payload)
    characters = string.ascii_letters  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    email = string.digits
    em =  "".join(choice(email) for x in range(randint(8, 8)))
    ii = string.digits
    id =  "".join(choice(ii) for x in range(randint(9, 12)))
    print(i)