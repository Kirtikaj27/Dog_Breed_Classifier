import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        output = run_app(image_bytes=img_bytes)

    return render_template('index.html', prediction_text=This is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)