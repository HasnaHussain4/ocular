import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg19 import preprocess_input

model = load_model('model.keras')

def predict_image(img):
    img = tf.io.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, size=[224, 224])
    # img = img / 255.0
    img = preprocess_input(img)
    img = tf.expand_dims(img, axis=0)
    prediction = model.predict(img)[0]
    return prediction

st.set_page_config(layout='wide')
st.markdown("<h1 style='text-align: center;'>Eye Disease Prediction</h1>", unsafe_allow_html=True)

file = st.file_uploader("Upload an image", type="jpg")

if file is not None:
    prediction = predict_image(file.getvalue())
    
    pred_category = tf.argmax(prediction).numpy()
    if pred_category == 0:
        pred_label = "Normal"
    elif pred_category == 1:
        pred_label = "Cataract"
    elif pred_category == 2:
        pred_label = "Diabetes"
    elif pred_category == 3:
        pred_label = "Glaucoma"
    elif pred_category == 4:
        pred_label = "Hypertension"
    elif pred_category == 5:
        pred_label = "Myopia"
    elif pred_category == 6:
        pred_label = "Age Issues"
    else:
        pred_label = "Unknown"

    st.write(f"Predicted Label: {pred_label}")
