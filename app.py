from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        text = file.read().decode('utf-8')
        sentiment = analyze_sentiment(text)
        return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
