import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Loading dataset
mnist = tf.keras.datasets.mnist
(_, _), (img_test, lbl_test) = mnist.load_data()

# Loading model
model = tf.keras.models.load_model('C:/Users/filal/Documents/GitHub/Neural-Network-Drawing/model/training_3.model')


# Predicting number
def predict(img):
    img = np.rot90(img, 1)
    img = np.flipud(img)
    prediction = model.predict([np.array([img])])
    print(np.argmax(prediction))