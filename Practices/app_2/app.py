from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from trainModel import f1Score, precisionScore, recallScore
from load_kdd import load_kdd_dataset
import pandas as pd

app = Flask(__name__)
CORS(app)

df = None

@app.route("/f1-Score", methods=["GET"])
@cross_origin()
def pred_f1Score():
    f1_Score = f1Score()
    f1Score_rounded = round(f1_Score, 3)
    return jsonify({'f1Score': f1Score_rounded})

@app.route("/precision-Score", methods=["GET"])
@cross_origin()
def pred_precisionScore():

    precision_Score = precisionScore()
    precisionScore_rounded = round(precision_Score, 3)
    return jsonify({'precisionScore': precisionScore_rounded})

@app.route("/recall-Score", methods=["GET"])
@cross_origin()
def pred_recallScore():
    recall_Score = recallScore()
    recallScore_rounded = round(recall_Score, 3)
    return jsonify({'recallScore': recallScore_rounded})

# @app.route("/loadDataset", methods=["GET"])
# def load_dataset():
#     global df
#     df = load_kdd_dataset("../../datasets/NSL-KDD/KDDTrain+.arff")
#     df.to_html("datasetLoad.html")
#     return jsonify({'message': "Dataset cargado"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
