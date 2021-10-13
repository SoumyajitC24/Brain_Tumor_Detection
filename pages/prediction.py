"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
import numpy as np

import tensorflow as tf
from tensorflow.keras import preprocessing
import cv2
from PIL import Image

from model import load_model

def app():
    """This function runs the prediction page"""

    # Create label values for the prediction
    label = ['glioma_tumor' , 'meningioma_tumor' , 'no_tumor' , 'pituitary_tumor']

    # Take image input
    image = st.file_uploader("Upload MRI scan image of Brain", type=['png','jpeg', 'jpg'])

    # If image then show the image and preprocess it.
    if image:
        st.image(image , width = 325)

        images = Image.open(image)
        images = np.array(images)
        img = cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)
        img = preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        # load the model
        model = load_model()

        # predict value
        pred_value = ""
        prediction = model.predict(img)
        pred_value = label[np.argmax(prediction)]

        # Show prediction values
        if(pred_value == 'no_tumor'):
            st.success("Congratulations! No tumor detected.")
        else:
            st.success(f"Predicted Brain Tumor category is '{pred_value}'")
        