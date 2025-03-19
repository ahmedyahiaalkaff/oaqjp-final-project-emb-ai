import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    json_body = { 'raw_document': {'text': text_to_analyze}}
    response = requests.post(url, json=json_body, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = format_response(response.text)
    return formatted_response

def format_response(response_text):
    json_dict = json.loads(response_text)
    scores = json_dict['emotionPredictions'][0]['emotion']
    max_score = 0
    dominant_emotion = ''
    for emotion in scores:
        if scores[emotion] >= max_score:
            max_score = scores[emotion]
            dominant_emotion = emotion
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
