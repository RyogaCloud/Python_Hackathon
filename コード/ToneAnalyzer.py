import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

tone_analyzer = ToneAnalyzerV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
tone_analyzer.set_service_url('{url}')

tone_analysis = tone_analyzer.tone(
    {'text': '{English sentence you want to analyze}'},
    content_type='application/json').get_result()

print(json.dumps(tone_analysis, indent=2))