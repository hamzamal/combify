# -*- coding: utf-8 -*-
"""server.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bagCfdP0TFBlL3innat9Cy3ilODfxzbA
"""

import keras
from flask import Flask, jsonify, request
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.callbacks import EarlyStopping
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
# load weights into new model
    model.load_weights("model.h5")
    df = pd.DataFrame(json, index=[0])
    max_features = 2000
    tokenizer = Tokenizer(num_words=max_features, split=' ')
    tokenizer.fit_on_texts(df.values)
    X = tokenizer.texts_to_sequences(df.values)
    X = pad_sequences(X)
    y_predict=model.predict(X)
    result = {"Predicted House Price" : y_predict[0]}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
