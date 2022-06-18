from flask import Flask
from predict import pipeline_audio 
import scipy.io.wavfile
app = Flask(__name__)

### Web Pages ###
@app.route("/")
def home():
    print("\n\nhere\n\n")
    

    rate, data = scipy.io.wavfile.read('a.wav')

    print(pipeline_audio(data))
    # return render_template("home.html")

@app.route("/about")
def about():
    print("\n\nhere\n\n")

    pass
    # return render_template("about.html")




if __name__ == '__main__':
    app.run(debug=True)
