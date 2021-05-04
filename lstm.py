# -*- coding: utf-8 -*-
"""lstm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1baYbuPzQ-pXS2eOCbTJ-ehK0XYJTmcu-
"""

import pandas as pd
import numpy as np
import string, re
import itertools
import nltk
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud,STOPWORDS
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.callbacks import EarlyStopping
import joblib

df=pd.read_csv("sample.csv.csv")

max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(df['filteredCleanedText'].values)
X = tokenizer.texts_to_sequences(df['filteredCleanedText'].values)
X = pad_sequences(X)

embed_dim = 64
lstm_out = 16
model = Sequential()
model.add(Embedding(max_features, embed_dim, input_length=X.shape[1]))
model.add(LSTM(lstm_out))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

Y = df['sentiment'].values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.1)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

batch_size = 16
model.fit(X_train,
          Y_train,
          epochs=6,
          batch_size=batch_size,
          validation_data=(X_test, Y_test),
          callbacks = [EarlyStopping(monitor='val_acc',
                       min_delta=0.001,
                       patience=2,
                       verbose=1)]
           )

joblib.dump(model, "rf_model.sav")