import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon='/Users/renadamer/Downloads/stream/mainpage_app/logo1.png',
)


import base64
import streamlit as st
import plotly.express as px
import cv2
import pytesseract
from PIL import Image
import numpy as np


df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("/Users/renadamer/Downloads/stream/logos.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://f.top4top.io/p_2887ex3731.gif");
background-size:100% 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:/Users/renadamer/Downloads/stream/logos.png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#st.sidebar.header("Pages")

#st.link_button("ابــــدأ", "http://localhost:8501/page_2")


#centered_button = """
#<div style="display: flex; justify-content: center; margin-top: 350px;">
 #   <button style="padding: 10px 20px; background-color: #008CBA; color: white; text-align: center;">Centered Button</button>
#</div>
#"""
#st.markdown(centered_button, unsafe_allow_html=True)



button_code = """
<div style="margin-top: 320px; display: flex; justify-content: center;">
    <a href="http://localhost:8501/page_2">
        <button style="padding: 10px 20px; background-color: #EBA1A6; color: white;border-radius: 20px; border: none;">ابــدأ</button>
    </a>
</div>
"""

st.markdown(button_code, unsafe_allow_html=True)