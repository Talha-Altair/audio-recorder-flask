from flask import *
import os

app = Flask(__name__)

AUDIO_OUTPUT_FOLDER = 'static/audio'

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        f = request.files['audio_data']
        with open(f'{AUDIO_OUTPUT_FOLDER}/audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        return render_template('index.html', request="POST")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)