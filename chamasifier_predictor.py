import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models


model = models.load_model('models/chamasifier_1.h5')



for i in range(100):
    img_pred = image.load_img('tester/test1/'+str(i)+'.jpeg',target_size=(150,150))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred,axis=0)
    result = model.predict(img_pred)
    if result[0][0] == 0:
        print(str(i) +" is JackFruit")
    else:
        print(str(i) +" Mango")





