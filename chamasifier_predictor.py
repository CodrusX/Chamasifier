# Importing necessary libraries and packeges
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models
import numpy as np
# Loading the model

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
model = models.load_model(os.path.join(APP_ROOT, 'models/chamasifier_1.h5'))

for i in range(100):
    img_pred = image.load_img(os.path.join(APP_ROOT,'tester/test1/'+str(i)+'.jpeg'),target_size=(150,150))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred,axis=0)
    result = model.predict(img_pred)
    if result[0][0] == 0:
        print(str(i) +" is JackFruit")
    else:
        print(str(i) +" Mango")




