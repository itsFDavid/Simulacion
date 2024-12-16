from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from predict import get_f1_score, get_f1_score_polynomial, get_f1_score_reduced

import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/f1-score-reduced", methods=["GET"])
def predict_f1_reduced():
    f1_score = get_f1_score_reduced()
    return jsonify({'f1_score': f1_score})


@app.route("/f1-score", methods=["GET"])
def predict_f1_score():
    f1_score = get_f1_score()
    return jsonify({'f1_score': f1_score})


@app.route("/f1-score-poly", methods=["GET"])
def predict_f1_score_poly():
    f1_score = get_f1_score_polynomial()
    return jsonify({'f1_score': f1_score})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000, debug=True)