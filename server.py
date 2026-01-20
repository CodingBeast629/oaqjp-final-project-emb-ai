"""
Flask server for Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Call emotion detector and format output as required.
    Includes error handling for blank / invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    # Task 7: handle invalid or blank input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
