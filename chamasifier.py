#Importing necessary libraries and packages

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import MaxPooling2D

# Create a neural network model

model = Sequential()  # inilializing CNN network

# adding first polling & convolution layer

model.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# adding second polling & convolution layer

model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add one flattened input layer for the pixels
model.add(Flatten())

# Add 5 dense hidden layers
# Add one dense output layer for the 2 photos

model.add(Dense(units=32,activation = 'relu'))
model.add(Dense(units=64,activation = 'relu'))
model.add(Dense(units=128,activation = 'relu'))
model.add(Dense(units=256,activation = 'relu'))
model.add(Dense(units=256,activation = 'relu'))
model.add(Dense(units=2,activation = 'sigmoid'))

#Compiling CNN
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#Fitting CNN to images

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255, # To rescaling the image in range of [0,1]
                                   shear_range = 0.2, # shear the images from current position
                                   zoom_range = 0.2, # To randomly zoom the images
                                   horizontal_flip = True) #  for randomly flipping half of the images horizontally

#Testing and training

test_datagen = ImageDataGenerator(rescale = 1./255)
print("\nTraining and testing the data...\n")
training_set = train_datagen.flow_from_directory('train',
                                                target_size=(64,64),
                                                batch_size=6, #Total no. of batches
                                                class_mode='binary')
test_set = test_datagen.flow_from_directory('test',
                                            target_size=(64,64),
                                            batch_size=12,
                                            class_mode='binary')

#training the model             error_here
model.fit_generator(
        training_set,
        validation_steps=35,
        epochs=5,
        validation_data=test_set,
        nb_val_samples=18)

#Saving the model

model.save("CNNmodel.h5")
