import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

MODEL_DIR = 'model'
MODEL_FILENAME = 'my_best_model.h5'
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

def load_saved_model(filename):
    saved_model = load_model(filename)
    return saved_model

def predict(saved_model, input_value):
    prediction = saved_model.predict([input_value])
    return prediction[0][0]

if __name__ == '__main__':
    saved_model = load_saved_model(MODEL_PATH)
    prediction = predict(saved_model, 10.0)
    print('Prediction:', prediction)