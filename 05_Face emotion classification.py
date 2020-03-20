from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model = Sequential()
model.add(Conv2D(32, (2, 2),
                 input_shape=(150, 150, 3), activation='relu')) # stride가 이미지 크기와 맞아떨어지지 않을 경우 맞는 부분만 계산(ex> (5, 5) => (2, 2))
model.add(Conv2D(128, (2, 2), activation='relu')) # Kernel의 크기는 input의 크기보다 작아야 한다!(같으면 안됨)
model.add(MaxPooling2D(2, 2))# MaxPooling은 최댓값이 겹치지 않도록(중요) stride를 알아서 조절해 데이터를 축소한다!(통상적으로 절반 ex> (6, 6) => (3, 3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])

# model.summary()

from keras.preprocessing.image import ImageDataGenerator

train_data = ImageDataGenerator(rescale=1./255, 
                                shear_range=0.2,
                                zoom_range=0.2,
                                horizontal_flip=True)
test_data = ImageDataGenerator(rescale=1./255)
train_set = train_data.flow_from_directory('C:/Users/User/Desktop/dataset/train',
                                           target_size=(150,150),
                                           batch_size=1,
                                           class_mode='binary')

test_set = test_data.flow_from_directory('C:/Users/User/Desktop/dataset/test',
                                           target_size=(150,150),
                                           batch_size=1,
                                           class_mode='binary')

model.fit_generator(train_set,
                    steps_per_epoch=10,
                    epochs=30,
                    validation_data=test_set,
                   validation_steps=32)

output = model.predict_generator(test_set, steps=5)
print(output)