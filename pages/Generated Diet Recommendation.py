import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64

# Function to convert the image to base64 encoding
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set a JPG as the background of the page
def set_background_image(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    [data-testid="stApp"] {{
    background-image: url("data:image/jpeg;base64,{bin_str}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_background_image('image2.jpg')

# Add content
st.markdown("<div style='text-align: center;'><h1 style='color: black;font-size: 80px;'>Page 2</h1></div>", unsafe_allow_html=True)

import streamlit as st

# Check if the diet recommendation is in session state
if 'diet_recommendation' in st.session_state:
    st.write("Diet Recommendation:")
    st.write(st.session_state['diet_recommendation'])
else:
    st.write("No diet recommendation available. Please go back and enter your details.")


