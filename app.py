import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

cat_img = Image.open("cat.png")
background_img = Image.open("skye.png")
background_base64 = img_to_base64(background_img)

st.markdown(
    f"""
    <style>
    @keyframes neon-flicker {{
        0%, 100% {{ text-shadow:
            0 0 5px #00ffff,
            0 0 10px #00ffff,
            0 0 20px #00ffff,
            0 0 40px #0ff,
            0 0 80px #0ff,
            0 0 90px #0ff,
            0 0 100px #0ff,
            0 0 150px #0ff; 
            color: #0ff; }}
        50% {{ text-shadow:
            0 0 2px #00ffff,
            0 0 5px #00ffff,
            0 0 10px #00ffff,
            0 0 20px #0ff; 
            color: #a0ffff; }}
    }}

    @keyframes fadeGlow {{
        0% {{ opacity: 0; text-shadow: none; }}
        100% {{ opacity: 1; text-shadow: 0 0 10px #0ff; }}
    }}

    .stApp {{
        background-image: url("data:image/png;base64,{background_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #0ff;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .container {{
        text-align: center;
        max-width: 800px;
        padding: 20px;
    }}
    .title {{
        font-size: 3.5rem;
        font-weight: 900;
        text-transform: uppercase;
        animation: neon-flicker 2.5s infinite alternate;
        margin-bottom: 2rem;
        letter-spacing: 0.1em;
        user-select: none;
    }}
    .cat-img {{
        width: 300px !important;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0, 255, 255, 0.7);
        margin-bottom: 2rem;
        transition: transform 0.3s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    .cat-img:hover {{
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 255, 255, 1);
    }}
    .links {{
        display: flex;
        justify-content: center;
        gap: 40px;
        font-size: 1.4rem;
        margin-bottom: 3rem;
        font-weight: 700;
        color: #0ff;
        text-shadow: 0 0 6px #0ff;
    }}
    .links a {{
        color: #0ff;
        text-decoration: none;
        padding: 8px 12px;
        border-radius: 8px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .links a:hover {{
        text-decoration: underline;
        text-shadow: 0 0 15px #0ff;
        background-color: rgba(0, 255, 255, 0.15);
    }}
    .footer {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-style: italic;
        font-size: 1.5rem;
        color: #0ff;
        animation: fadeGlow 3s ease forwards;
        opacity: 0;
        user-select: none;
    }}

    @media (max-width: 600px) {{
        .title {{
            font-size: 2.5rem;
            white-space: normal;
        }}
        .cat-img {{
            width: 80vw !important;
            margin-bottom: 1.5rem;
        }}
        .links {{
            gap: 20px;
            font-size: 1.1rem;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }}
        .footer {{
            font-size: 1.2rem;
            padding-top: 30px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">🐾 DUBZZZ_VALO\'S STREAMING HUB</div>', unsafe_allow_html=True)

st.markdown(f'<img src="data:image/png;base64,{img_to_base64(cat_img)}" class="cat-img" alt="Cat Image" />', unsafe_allow_html=True)

st.markdown(
    """
    <div class="links">
        <a href="https://youtube.com" target="_blank">🎥 YouTube</a>
        <a href="https://instagram.com" target="_blank">📸 Instagram</a>
        <a href="https://tiktok.com" target="_blank">🎵 TikTok</a>
        <a href="https://twitch.tv" target="_blank">🎮 Twitch</a>
    </div>
    <div class="footer">
        Thanks for stopping by! Catch more epic streams soon 🙏✨
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
