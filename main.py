from flask import Flask
from predict import pipeline_audio 
import librosa
app = Flask(__name__)

### Web Pages ###
@app.route("/")
def home():
    print("\n\nhere\n\n")
    file_name="a.wav"
    y, sr = librosa.load(file_name,sr=None)
    print(pipeline_audio(y))
    # return render_template("home.html")

@app.route("/about")
def about():
    print("\n\nhere\n\n")

    pass
    # return render_template("about.html")




if __name__ == '__main__':
    app.run(debug=True)
