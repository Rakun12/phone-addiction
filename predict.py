import pickle
from flask import Flask, request, jsonify

model_file = 'model_nbgaussian.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('phone_addiction')

@app.route('/predict', methods=['POST'])
def predict():
    user = request.get_json()

    X = dv.transform([user])
    y_pred = (model.predict_proba(X)).round(3)
    addiction_level = model.predict(X)

    result = {
        'addiction_probability [0]': float(y_pred[0][0]),
        'addiction_probability [1]': float(y_pred[0][1]),
        'addiction_probability [2]': float(y_pred[0][2]),
        'addiction_probability [3]': float(y_pred[0][3]),
        'addiction_probability [4]': float(y_pred[0][4]),
        'addiction_level': int(addiction_level)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1212)
