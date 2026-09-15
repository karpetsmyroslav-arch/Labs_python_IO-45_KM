"""
Модуль реалізує веб-сервер на базі Flask для виявлення емоцій.
Надає маршрути для відображення головної сторінки та обробки
запитів на аналіз тексту через пакет EmotionDetection.
"""
from flask import Flask
from flask import render_template
from flask import request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render():
    """
    Обробляє маршрут головної сторінки та рендерить шаблон index.html.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detector_server():
    """
    Отримує текст із запиту, передає його у функцію emotion_detector,
    обробляє можливі помилки (порожній ввід) та повертає форматований
    результат з оцінками емоцій.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response['dominant_emotion']
    return (
        f"System response for this statement: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} та 'sadness': {sadness}. "
        f"dominant_emotion - {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
