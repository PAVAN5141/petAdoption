
import flask
from flask import Flask, request,jsonify, render_template
import pickle

app=flask.Flask(__name__)
app.config["DEBUG"]=False

from flask_cors import CORS, cross_origin
CORS(app)

@app.route('/')
@cross_origin()

def home():
    return '<h> Which Pet and breed are you looking for... <\h>'

@app.route('/predict_breed')
def predict_breed():
    from sklearn.externals import joblib
    model_1= joblib.load('Breed_Classification.ml')
    Breed_Class=model_1.predict([[2.0,4,1,1,18,13,9]])
    return str(Breed_Class)

@app.route('/predict_pet')
def predict_pet():
    from sklearn.externals import joblib
    model_2=joblib.load('Pet_Classification.ml')
    Pet_Class=model_2.predict([[2.0,4,1,1,18,13,9]])
    return str(Pet_Class)

if __name__=="__main__":
    app.run(debug=False)





