import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenator#prolly wont need this one

import cv2
import matplotlib as plt


img_height = 28
img_width = 28
batch_size = 2

model = keras.Sequential([
    layers.Input((28,28,1)),
    layers.Conv2D(16,3,padding='same'),
    layers.Conv2D(32,3,padding='same'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(10)
])