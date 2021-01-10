import streamlit as st
import pandas as pd
import numpy as np
import os, urllib, cv2

# # This function loads an image from public repo on S3. We use st.cache on this
# # function as well, so we can reuse the images across runs.
# @st.cache(show_spinner=False)
# def load_image(url):
#     with urllib.request.urlopen(url) as response:
#         image = np.asarray(bytearray(response.read()), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     image = image[:, :, [2, 1, 0]] # BGR -> RGB
#     return image

# This implementation reads local images
@st.cache()
def load_sim_image(path):
    with open(path,'rb') as f:
        image = f.read()
    # image = cv2.imread(path)
    image = np.asarray(bytearray(image), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = image[:, :, [2, 1, 0]] # BGR -> RGB
    return image

# # Path to the public S3 bucket
# DATA_URL_ROOT = "https://self-driving-dataset.s3-us-west-2.amazonaws.com/Ch2_001/center/"
# list_frame = pd.read_csv('Ch2_001/final_example.csv')

# Path to the local folder
list_frame = pd.read_csv(os.path.join(os.getcwd(),'term1-simulator-windows','sim_data', 'driving_log.csv'), names=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed'])


# Center panel
st.markdown("# Simulation dataset viewer")

id = st.slider("Frame",0,len(list_frame),0)

left_frame = str(list_frame.left[id])
center_frame = str(list_frame.center[id])
right_frame = str(list_frame.right[id])

# col1,col2=st.beta_columns(2)

# col1.markdown("## Left camera")
# left_image = load_sim_image(left_frame)
# col1.image(left_image)

# col2.markdown("## Right camera")
# right_image = load_sim_image(right_frame)
# col2.image(right_image)


col1,col2,col3=st.beta_columns(3)

col1.markdown("## Left camera")
left_image = load_sim_image(left_frame)
col1.image(left_image)

col2.markdown("## Center camera")
center_image = load_sim_image(center_frame)
col2.image(center_image)

col3.markdown("## Right camera")
right_image = load_sim_image(right_frame)
col3.image(right_image)

st.markdown("## Steering:"+str(list_frame.steering[id])+" - Throttle:"+str(list_frame.throttle[id])+" - Speed:"+str(list_frame.speed[id]))

# # Sidebar
# st.sidebar.title("Self driving simulation")

# st.sidebar.markdown("## Center camera")
# center_image = load_sim_image(center_frame)
# st.sidebar.image(center_image)

# st.sidebar.write(list_frame[['steering','throttle','reverse','speed']])

# image_url = os.path.join(DATA_URL_ROOT, selected_frame)
# image_path = os.path.join(DATA_URL_ROOT, selected_frame)

