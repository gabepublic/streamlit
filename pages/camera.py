import streamlit as st
from PIL import Image
import numpy as np
import io
import base64


st.set_page_config(
    page_title = "Streamlit Sandbox",
    page_icon = "favicon.ico",
    layout = "centered",     # centered, wide
    initial_sidebar_state = "collapsed",    # expanded, collapsed, auto
    menu_items = {
        "Get Help": "https://docs.streamlit.io/",
        "About": "Streamlit Sandbox for experiments"
    }
)

st.sidebar.title("Camera")
picture = st.camera_input("Take a picture")

if picture is not None:
    st.image(picture)
    # To read image file buffer as a PIL Image:
    img = Image.open(picture)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)

    # Convert the numpy array to a PIL Image object
    #image = Image.fromarray(img_array)

    # Save the image to a JPG file
    img.save('output_image.jpg', format="JPEG")

    # Save the image to a BytesIO object
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")

    # Encode the image bytes using base64
    img_str = base64.b64encode(buffered.getvalue())

    # To convert it back to a string (optional, for readability)
    img_base64 = img_str.decode('utf-8')

