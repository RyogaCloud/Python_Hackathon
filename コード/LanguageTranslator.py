import json
from ibm_watson import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='{version}',
    iam_apikey='{apikey}',
    url='{url}')

translation = language_translator.translate(
    text='{Japanese you want to translate into English}',
    model_id='ja-en').get_result()

print(json.dumps(translation, indent=2))