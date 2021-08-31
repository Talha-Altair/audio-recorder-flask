from flask import *
import pandas as pd
import os

app = Flask(__name__)

AUDIO_OUTPUT_FOLDER = 'static/audio'

def get_data():

    df = pd.read_csv('questions.csv')

    questions_list = df.questions.to_list()

    return questions_list

@app.route("/", methods=['POST', 'GET'])
def index():

    questions_list = get_data()

    if request.method == "POST":

        f = request.files['audio_data']

        with open(f'{AUDIO_OUTPUT_FOLDER}/audio.wav', 'wb') as audio:

            f.save(audio)

        print('file uploaded successfully')

        return render_template('index.html')

    return render_template("index.html", questions = questions_list)

@app.route("/upload", methods=['POST', 'GET'])
def upload():

    questions_list = get_data()

    if request.method == "POST":

        f = request.files['audio_data']

        name = request.values.get("name")

        print(name)

        with open(f'{AUDIO_OUTPUT_FOLDER}/{name}.wav', 'wb') as audio:

            f.save(audio)

        print('file uploaded successfully')

    return render_template("index.html", questions = questions_list) 

if __name__ == "__main__":
    
    app.run(debug=True)