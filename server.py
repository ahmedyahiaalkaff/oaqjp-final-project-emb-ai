"""
This is the emotion detection flask app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def index():
    """
    This is the handler of the index
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    This is the handler of emotion detection requests
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        response = emotion_detector(text_to_analyze)
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        return f"For the given statement, the system reponse is \
                 'anger': {response['anger']}, \
                 'disgust': {response['disgust']}, \
                 'fear': {response['fear']}, \
                 'joy': {response['joy']}, \
                 'sadness': {response['sadness']}. \
                 The dominant emotion is {response['dominant_emotion']}."
    return "Invalid text! Please try again!"

app.run(host='0.0.0.0', port=5000)
