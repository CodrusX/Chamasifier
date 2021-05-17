import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models
import numpy as np


model = models.load_model('models/chamasifier_1.h5')

img_pred = image.load_img('tester/mango.jpg',target_size=(150,150))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred,axis=0)

result = model.predict(img_pred)
if result[0][0] == 0:
    print("JackFruit")
else:
    print("Mango")