from flask import Flask, render_template, request
import pickle
import numpy as np
from model import HousePricePrediction  # 🔑 REQUIRED
Model = HousePricePrediction()
app = Flask(__name__)

@app.route('/')
def sample():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def fun3():
    features = [float(i) for i in request.form.values()]
    prediction = Model.predict(features)
    return render_template(
        'index.html',
        prediction_text=f'Predicted Price: {prediction}'
    )

if __name__ == '__main__':
    app.run(debug=True)
