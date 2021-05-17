# Importing necessary libraries and packeges

from tensorflow.keras.preprocessing import image
from tensorflow.keras import models
import numpy as np

# Loading the model

model = models.load_model('models/chamasifier_1.h5')

# Loading the image

img_pred = image.load_img('tester/mango.jpg',target_size=(150,150))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred,axis=0)

# Testing the image

result = model.predict(img_pred)

# Printing the output

if result[0][0] == 0:
    print("JackFruit")
else:
    print("Mango")
