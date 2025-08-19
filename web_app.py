import cv2
import numpy as np
import tempfile
import streamlit as st
from main import image_background_remove

st.title("welcome to image background remover")


uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # save to a temp file so OpenCV can read it
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp_file.write(uploaded_file.read())
    temp_file_path = temp_file.name

    output = image_background_remove(temp_file_path)  # ✅ pass path
    st.image(output, channels="BGR")



# here the main web function using streamlit.. without any fancy UI.. app.py is basically main web app