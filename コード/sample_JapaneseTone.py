import json
from ibm_watson import LanguageTranslatorV3, ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
language_translator.set_service_url('{url}')

tone_analyzer = ToneAnalyzerV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
tone_analyzer.set_service_url('{url}')

translation = language_translator.translate(
    text='{Japanese sentence you want to analyze}',
    model_id='ja-en').get_result()

tone_analysis = tone_analyzer.tone(
    {'text': str(translation['translations'][0]['translation'])},
    content_type='application/json').get_result()

print(json.dumps(tone_analysis, indent=2))