from flask import *
import pandas as pd
import os

app = Flask(__name__)

AUDIO_OUTPUT_FOLDER = 'static/audio'

df = pd.read_csv('questions.csv')

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        f = request.files['audio_data']
        with open(f'{AUDIO_OUTPUT_FOLDER}/audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        return render_template('index.html', request="POST")

    questions_list = df.questions.to_list()

    print(questions_list,type(questions_list))

    return render_template("index.html", questions = questions_list)

if __name__ == "__main__":
    app.run(debug=True)