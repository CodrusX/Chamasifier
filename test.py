from tensorflow.keras import models
import numpy as np
import cv2


model = models.load_model("CNNmodel.h5")

img = cv2.imread('tester/mango.jpg')

img = cv2.resize(img,(64,64))

img = np.reshape(img,[1,64,64,3])


classes = np.argmax(model.predict(img),axis=-1)

if(classes == [0]):
    print("Jackfruit")
else:
    print("Mango")

