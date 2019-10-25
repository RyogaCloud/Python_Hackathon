import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
language_translator.set_service_url('{url}')

translation = language_translator.translate(
    text='{Japanese you want to translate into English}',
    model_id='ja-en').get_result()

print(json.dumps(translation, indent=2))