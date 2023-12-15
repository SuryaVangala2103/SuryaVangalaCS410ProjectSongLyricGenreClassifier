import pickle

from model import prepare_input
from flask import Flask, render_template, request

#initialize flask app
app = Flask(__name__)
#unpickle model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

#this establishes the predict function in the url signature, and gives it get and post functionality
@app.route("/predict",methods=['GET', 'POST'])
def predict():
    #post functionality requires processing input and returning prediction
    if request.method == 'POST':
        # I obtain the text from the request and run my prepare_input function
        lyrics = prepare_input(request.form["Lyrics"], vectorizer)
        #the model returns a one element list of a label as the output. I access the element with [0]
        prediction = model.predict(lyrics)[0]
        #the model outputs the correct text already, just assemble the output string
        text_output = "Genre: " + prediction
        #return statement renders html template and includes prediction text
        return render_template("template1.html", prediction_text=text_output)
    # get functionality requires displaying text window for input submission
    else:
        #display webpage template
        return render_template("template1.html")


if __name__ == "__main__":
    #run app
    app.run()
