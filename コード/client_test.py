import requests
import json

URL = '{send_URL}'

def send_bpm(userID, text):
    #POSTパラメータは二つ目の引数に辞書で指定する
    response = requests.post(
        URL,
        {'userID': userID, 'text': text},
        headers={'Content-Type': 'text/html'})    

if __name__=='__main__':
    send_bpm('144561', '144')