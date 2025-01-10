from flask import Flask, jsonify
from tree_decision import evaluate_model_with_train_set, evaluate_model_with_val_set


app = Flask(__name__)


@app.route('/predict-test-set', methods=['GET'])
def predict_test_set():
    return jsonify({"f1-score": evaluate_model_with_train_set()})


@app.route('/predict-val-set', methods=['GET'])
def predict_vak_set():
    return jsonify({"f1-score": evaluate_model_with_val_set()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
