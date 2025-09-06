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
        color: #87CEFA;
        text-decoration: none;
        padding: 8px 12px;
        border-radius: 6px;
        transition: background-color 0.2s ease;
    }}
    .links a:hover {{
        background-color: rgba(135, 206, 250, 0.3);
    }}
    .footer {{
        font-style: italic;
        font-size: 1.2rem;
        color: #ddd;
        padding-bottom: 20px;
    }}

    /* Responsive */
    @media (max-width: 600px) {{
        .title {{
            font-size: 2rem;
        }}
        .title .star {{
            font-size: 2rem;
        }}
        .cat-img {{
            width: 80vw !important;
            margin-bottom: 1rem;
        }}
        .links {{
            gap: 20px;
            font-size: 1.1rem;
            flex-wrap: wrap;
        }}
        .footer {{
            font-size: 1rem;
            padding-bottom: 40px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container with flexbox for center alignment
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# Title + star emoji side by side
st.markdown('<div class="title">🐾 Dubzzz_Valo\'s Streaming Hub <span class="star">🌟</span></div>', unsafe_allow_html=True)

# Cat image with class for styling
st.markdown(f'<img src="data:image/png;base64,{img_to_base64(cat_img)}" class="cat-img" alt="Cat Image" />', unsafe_allow_html=True)

# Social media links spaced horizontally with hover effect
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
