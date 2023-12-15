import pickle

from model import prepare_input
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route("/predict",methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        lyrics = prepare_input(request.form["Lyrics"], vectorizer)
        prediction = model.predict(lyrics)[0]
        text_output = "Genre: " + prediction
        return render_template("template1.html", prediction_text=text_output)
    else:
        return render_template("template1.html")


if __name__ == "__main__":
    app.run()
