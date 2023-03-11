import tensorflow as tf
from tensorflow.keras.models import save_model
import numpy as np
from tensorflow import keras
import os

MODEL_DIR = 'model'
MODEL_FILENAME = 'my_best_model.h5'
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

def create_model():
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    return model

def get_data():
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
    return xs, ys

def train_model(model, xs, ys):
    model.fit(xs, ys, epochs=500)

def save_model_custom(model, filename):
    save_model(model, filename)
    print('Model saved as: ', filename)

if __name__ == '__main__':
    os.makedirs(MODEL_DIR, exist_ok=True)
    model = create_model()
    xs, ys = get_data()
    train_model(model, xs, ys)
    save_model(model, MODEL_PATH)

