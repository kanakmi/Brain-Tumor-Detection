import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import backend as K

'''
Loading the Classifier Model from the disk
'''
with open('classifier_model.json', 'r') as json_file:
    json_savedModel = json_file.read()

# load the model architecture
model = tf.keras.models.model_from_json(json_savedModel)
model.load_weights('classifier_weights.h5')
opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt,loss="categorical_crossentropy", metrics=["accuracy"])

'''
Loading the Localization Model from the disk
'''
with open('localization_model.json', 'r') as json_file:
    json_savedModel= json_file.read()

# load the model architecture 
localize_model = tf.keras.models.model_from_json(json_savedModel)
localize_model.load_weights('localization_weights.h5')
localize_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

'''
Function to classify image as Tumor or Not and Localize in case of Tumor found
'''
def identify_tumor(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(128,128))
    img = np.array(img)
    img = img/255
    img = img.reshape((1, 128, 128, 3))
    predictions = model.predict(img)
    predicted = np.argmax(predictions[0])
    probablity = predictions[0][predicted]

    labels = {0: 'No Tumor', 1: 'Tumor'}
    result = {
        'class': labels[predicted],
        'probablity': probablity
    }

    if predicted==1:
        localize_tumor(file_path)

    return result

'''
Function to Localize Tumor in case of Tumor found
'''
def localize_tumor(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(256,256))
    img = np.array(img)
    img = img/255
    img = img.reshape((1, 256, 256, 3))
    predictions = localize_model.predict(img)
    img = np.squeeze(predictions[0])
    img = img*255
    img = img.astype('uint8')
    cv2.imwrite("mask_output.png", img)
