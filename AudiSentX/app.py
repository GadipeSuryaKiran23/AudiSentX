from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to map sentiment polarity to six emotions
def analyze_emotion(text):
    sentiment = TextBlob(text).sentiment.polarity
    
    if sentiment > 0.75:
        return 'Very Happy 😊'
    elif 0.5 < sentiment <= 0.75:
        return 'Happy 😄'
    elif -0.5 < sentiment <= 0.5:
        return 'Neutral 😐'
    elif -0.75 < sentiment <= -0.5:
        return 'Sad 😔'
    elif sentiment <= -0.75:
        return 'Very Angry 😠'
    else:
        return 'Angry 😡'

# Flask route for analyzing the emotion
@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion_route():
    data = request.get_json()
    text = data['text']
    emotion = analyze_emotion(text)
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
