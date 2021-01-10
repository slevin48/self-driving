import streamlit as st
import pandas as pd
import numpy as np
import os, urllib, cv2

# This function loads an image from Streamlit public repo on S3. We use st.cache on this
# function as well, so we can reuse the images across runs.
@st.cache(show_spinner=False)
def load_image(url):
    with urllib.request.urlopen(url) as response:
        image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = image[:, :, [2, 1, 0]] # BGR -> RGB
    return image

# Path to the public S3 bucket
DATA_URL_ROOT = "https://self-driving-dataset.s3-us-west-2.amazonaws.com/Ch2_001/center/"
list_frame = pd.read_csv('Ch2_001/final_example.csv')

st.sidebar.title("Self driving dataset")
id = st.sidebar.slider("Frame",0,len(list_frame),0)
st.sidebar.markdown("## Steering angle:")
st.sidebar.write(list_frame.steering_angle[id])
selected_frame = str(list_frame.frame_id[id])+".jpg"

image_url = os.path.join(DATA_URL_ROOT, selected_frame)
image = load_image(image_url)
st.image(image)