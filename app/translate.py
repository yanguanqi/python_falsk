import requests
from flask_babel import _

from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from={}&to={}'.format(source_language, dest_language)
    constructed_url = base_url + path + params
    headers = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'], 'Content-Type': 'application/json'}
    body = [{'text': text}]
    r = requests.post(constructed_url, headers=headers, json=body)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']
