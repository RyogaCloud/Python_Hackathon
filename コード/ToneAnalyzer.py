import json
from ibm_watson import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='{version}',
    iam_apikey='{apikey}',
    url='{url}')

tone_analysis = tone_analyzer.tone(
    {'text': '{English sentence you want to analyze}'},
    content_type='application/json').get_result()

print(json.dumps(tone_analysis, indent=2))