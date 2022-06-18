from flask import Flask, render_template
from predict import pipeline_audio 
import librosa
app = Flask(__name__)

### Web Pages ###
@app.route("/")
def home():
    file_name="a.wav"
    y, sr = librosa.load(file_name,sr=None)
    print(pipeline_audio(y))
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")




if __name__ == '__main__':
    app.run(debug=True)
