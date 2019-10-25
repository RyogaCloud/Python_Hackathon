# coding: UTF-8

from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import random
import json
from ibm_watson import ToneAnalyzerV3, LanguageTranslatorV3, PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests

language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
language_translator.set_service_url('{url}')

tone_analyzer = ToneAnalyzerV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
tone_analyzer.set_service_url('{url}')

personality_insights = PersonalityInsightsV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
personality_insights.set_service_url('{url}')

URL_message = '{send_url}'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

cred = credentials.Certificate('{firebase_key}')
app_firebase = firebase_admin.initialize_app(cred) 
db = firestore.client()

@app.route('/LINE', methods=['POST'])
def post_firebase_json():
    # json = request.get_json()  # POSTされたJSONを取得
    text = request.form['text']
    userID = request.form['userID']
  
    ran = random.randint(1, 100000)
    new_ref = db.collection('user').document(str(ran))
    new_data = {
        'userID': userID,
        'text': text
    }
    new_ref.set(new_data)

    return jsonify(json)

    # 英語に翻訳
    translation = language_translator.translate(
        text = text,
        model_id = 'ja-en'
    ).get_result()

    # 感情推定
    tone_analysis = tone_analyzer.tone(
        {'text': str(translation['translations'][0]['translation'])},
        content_type='application/json'
    ).get_result()

    payload_message = {
        "message": text
    }
    requests.post(URL_message, payload_message)

    if str(tone_analysis['document_tone']['tones'][0]['tone_id']) == 'joy':
        payload_message = {
            "message": '楽しそう',
            "facenum": 9
        }
        requests.post(URL_message, payload_message)
    elif str(tone_analysis['document_tone']['tones'][0]['tone_id']) == 'sadness':
        payload_message = {
            "message": '悲しまないで',
            "facenum": 19
        }
        requests.post(URL_message, payload_message)
    elif str(tone_analysis['document_tone']['tones'][0]['tone_id']) == 'anger':
        payload_message = {
            "message": '怒らないで',
            "facenum": 5
        }
        requests.post(URL_message, payload_message)
    elif str(tone_analysis['document_tone']['tones'][0]['tone_id']) == 'disgust':
        payload_message = {
            "message": '嫌がらないで',
            "facenum": 7
        }
        requests.post(URL_message, payload_message)
    else:
        payload_message = {
            "message": 'そうなんだ',
            "facenum": 0
        }
        requests.post(URL_message, payload_message)


@app.route('/LINE_judge', methods=['POST'])
def post_firebase_json_judge():
    json = request.get_json()  # POSTされたJSONを取得
    userID = str(json['userID'])
    text = str(json['text'])
    judge = str(json['judge'])
    number = judge.split(',')
    
    # firebase格納  
    ran = random.randint(1, 100000)
    new_ref = db.collection('user').document(str(ran))
    new_data = {
        'userID': userID,
        'text': text
    }
    new_ref.set(new_data)

    # firebaseから全ての内容を取り出し
    ref = db.collection('user')
    docs = ref.get()
    data_all = ''
    for doc in docs:
        data = doc.to_dict()
        
        translation = language_translator.translate(
            text = data['text'],
            model_id = 'ja-en'
        ).get_result()
        tone_analysis = tone_analyzer.tone(
            {'text': str(translation['translations'][0]['translation'])},
            content_type='application/json'
        ).get_result()

        if str(data['userID']) == userID:
            data_all += str(data['text'])

    with open('./personality.txt', mode='w') as f:
        f.write(data_all)

    with open('./personality.txt', mode='r') as profile_text:
        profile = personality_insights.profile(
            profile_text.read(),
            content_type='text/plain',
            consumption_preferences=True,
            raw_scores=True,
            accept='application/json',
            content_language='ja'
        ).get_result()
    
    if float(profile['personality'][0]['percentile']) > 0.7:
        print(str(profile['personality'][0]['name']))
    else :
        print('aaaaaaa')
    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=True)