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

# Apply CSS styles
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
    }}
    .center-container {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;  /* vertical centering */
        align-items: center;      /* horizontal centering */
        color: white;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
    }}
    .title {{
        font-size: 3rem;
        font-weight: 700;
        color: #FF4500;
        margin-bottom: 2rem;
    }}
    .links a {{
        margin: 0 15px;
        font-size: 1.3rem;
        color: #87CEFA;
        text-decoration: none;
    }}
    .footer {{
        margin-top: 2rem;
        font-style: italic;
        font-size: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# Title on top
st.markdown('<div class="title">🐾 Dubzzz_Valo\'s Streaming Hub 🌟</div>', unsafe_allow_html=True)

# Centered cat image
st.image(cat_img, width=250, caption="Cat", output_format="PNG")

# Links below cat image
st.markdown(
    """
    <div class="links">
        🎥 <a href="https://youtube.com" target="_blank">YouTube</a>
        📸 <a href="https://instagram.com" target="_blank">Instagram</a>
        🎵 <a href="https://tiktok.com" target="_blank">TikTok</a>
        🎮 <a href="https://twitch.tv" target="_blank">Twitch</a>
    </div>
    <div class="footer">
        Thanks for stopping by! Follow for more content 🙏
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
