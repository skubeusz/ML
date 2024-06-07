
## IMPORT BIBLIOTEK
from flask import Flask, jsonify, request 
import pickle


## FLASK
app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/ML', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)