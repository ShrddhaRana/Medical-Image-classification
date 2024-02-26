from keras.models import load_model
import sys
from tensorflow.keras.preprocessing import image
import numpy as np

class_names = ['lung_cancer', 'invalid', 'brain_tumor', 'bone_fracture']


model = load_model('./models/vgg16_medical_image_classifier.h5')

threshold = 0.005


def resize_image(image_path):
    img = image.load_img(image_path, target_size=(200, 200))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values to [0, 1]
    return img



def classify_image(image_path):
    image_path = '.' + image_path
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values to [0, 1]

    # Predict the class probabilities
    predictions = model.predict(img)
    print(predictions)
    # Get the predicted class
    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    print("Max : ", predictions[0][predicted_index])
    #fixing
    #fixing


    if predicted_class == 'brain_tumor':
        result = detect_brain_tumor(img)
    elif predicted_class == 'lung_cancer':
        result = detect_lung_cancer(img)
    elif predicted_class == 'bone_fracture':
        result = detect_bone_fracture(img)
    elif predicted_class == 'breast_cancer':
        result = detect_bone_fracture(img)
    else:
        return 'Invalid', 0.1

    predicted_class = predicted_class.replace('_', ' ')
    predicted_class = predicted_class.title()
    result = round(result, 3)
    return predicted_class, result


def detect_brain_tumor(img):
    model = load_model('./models/brain_tumor_vgg16.h5')
    prediction = model.predict(img)
    return prediction[0][0]


def detect_lung_cancer(img):
    model = load_model('./models/lung_cancer_vgg16.h5')
    prediction = model.predict(img)
    return prediction[0][0]


def detect_bone_fracture(img):
    model = load_model('./models/bone_fracture_vgg16.h5')
    prediction = model.predict(img)
    return prediction[0][0]


def detect_breast_cancer(img):
    model = load_model('./models/breast_cancer_vgg16.h5')
    prediction = model.predict(img)
    return prediction[0][0]

