from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from trainModel import predict

app = Flask(__name__)
CORS(app)

@app.route("/anomaly-predict", methods=["GET"])
@cross_origin()
def pred_anomaly():
    f1Score = predict()
    f1Score_rounded = round(f1Score, 3)
    return jsonify({'f1Score': f1Score_rounded})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)