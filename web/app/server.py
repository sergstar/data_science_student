from flask import Flask, request, jsonify
import pickle
import numpy as np

# загружаем модель из файла
with open('models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json).reshape(1, 4)
    return {'prediction': model.predict(features)[0]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)