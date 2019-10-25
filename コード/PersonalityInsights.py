from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    version='{version}',
    authenticator=IAMAuthenticator('{apikey}'))
personality_insights.set_service_url('{url}')

with open(join(dirname(__file__), '{file_path}')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(),
        'application/json',
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()

print(json.dumps(profile, indent=2))