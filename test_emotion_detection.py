"""
Unit tests for EmotionDetection package.
"""

from EmotionDetection import emotion_detector


def test_emotion_detector():
    """
    Tests emotion_detector against predefined statements and
    their expected dominant emotions.
    """
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear",
    }

    for statement, expected_emotion in test_cases.items():
        result = emotion_detector(statement)
        assert result["dominant_emotion"] == expected_emotion, (
            f"Failed for statement: '{statement}'"
        )


if __name__ == "__main__":
    test_emotion_detector()
    print("All unit tests passed!")
