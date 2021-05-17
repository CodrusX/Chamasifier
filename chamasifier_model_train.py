from tensorflow.keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as back


img_width = 150
img_height = 150
train_data_dir = 'data/train'
test_data_dir = 'data/test'
train_samples = 600
val_samples = 250
epoches = 200
batch_size = 25

if back.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

train_data_gen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True, vertical_flip=True, rotation_range=0.5,
)

test_data_gen = ImageDataGenerator(rescale=1./255)

train_generator = train_data_gen.flow_from_directory(directory=train_data_dir,
                                                     save_format='jpeg',
                                                     target_size=(
                                                         img_width, img_height),
                                                     classes=[
                                                         'jackfruit', 'mango'],
                                                     class_mode='binary',
                                                     batch_size=batch_size)

test_generator = test_data_gen.flow_from_directory(directory=test_data_dir,
                                                   save_format='jpeg',
                                                   target_size=(
                                                       img_width, img_height),
                                                   classes=[
                                                       'jackfruit', 'mango'],
                                                   class_mode='binary',
                                                   batch_size=batch_size)


# step-2 : build model

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', metrics=['accuracy'])

print('model complied!!')

print('starting training....')
training = model.fit_generator(generator=train_generator, steps_per_epoch=train_samples // batch_size,
                               epochs=epoches, validation_data=test_generator, validation_steps=val_samples//batch_size)

print('training finished!!')

print('saving weights to chamasifier_1.h5')

model.save('models/chamasifier_1.h5')

print('all weights saved successfully !!')


