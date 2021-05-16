from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = models.load_model("CNNmodel.h5")

test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory('test',
                                            target_size=(64, 64),
                                            save_format='jpg',
                                            class_mode='categorical',
                                            batch_size=12,
                                            )
result = model.predict_generator(test_set,verbose=0)

print(result)