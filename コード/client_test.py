import requests
import json

URL = '{send_url}'

def send_bpm(userID, text):
    #POSTパラメータは二つ目の引数に辞書で指定する
    response = requests.post(
        URL,
        # json.dumps({'userID': userID, 'text': text}),
        {'userID': userID, 'text': text})
        # headers={'Content-Type': 'multipart/form-data'})  
        # headers={'Content-Type': 'application/json'})  

if __name__=='__main__':
    send_bpm('165561', '144')