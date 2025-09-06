import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load images
cat_img = Image.open("cat.png")
background_img = Image.open("skye.png")

background_base64 = img_to_base64(background_img)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{background_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.85);
    }}
    .center-container {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 0 20px;
    }}
    .title {{
        font-size: 3rem;
        font-weight: 700;
        color: #FF4500;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
        justify-content: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
    }}
    .title .star {{
        font-size: 2.5rem;
    }}
    .cat-img {{
        width: 300px !important;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(255, 69, 0, 0.7);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }}
    .cat-img:hover {{
        transform: scale(1.05);
    }}
    .links {{
        display: flex;
        gap: 40px;
        justify-content: center;
        font-size: 1.4rem;
        margin-bottom: 2rem;
    }}
    .links a {{
