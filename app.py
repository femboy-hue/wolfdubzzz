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
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Pacifico&display=swap');

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
        background: linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCB77, #4D96FF);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 8s ease infinite;
        text-shadow: 0 0 10px rgba(255,255,255,0.8);
        margin-bottom: 2rem;
        white-space: nowrap;
        user-select: none;
    }}
    @keyframes gradientShift {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}
    .cat-img {{
        width: 300px !important;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6);
        margin-bottom: 2rem;
        transition: transform 0.3s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    .cat-img:hover {{
        transform: scale(1.05);
    }}
    .links {{
        display: flex;
        justify-content: center;
        gap: 40px;
        font-size: 1.4rem;
        margin-bottom: 3rem;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #87CEFA;
        text-shadow: 0 0 4px rgba(135, 206, 250, 0.7);
    }}
    .links a {{
        color: #87CEFA;
        text-decoration: none;
        padding: 8px 12px;
        border-radius: 6px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .links a:hover {{
        text-decoration: underline;
        text-shadow: 0 0 10px #87CEFA;
        background-color: rgba(135, 206, 250, 0.2);
    }}
    .footer {{
        font-family: 'Dancing Script', cursive;
        font-style: normal;
        font-size: 1.8rem;
        color: #FFD700;
        padding-top: 20px;
        text-shadow:
            0 0 5px #FFD700,
            0 0 10px #FFA500,
            0 0 20px #FF8C00;
        user-select: none;
        animation: glow 2.5s ease-in-out infinite alternate;
    }}
    @keyframes glow {{
        from {{
            text-shadow:
                0 0 5px #FFD700,
                0 0 10px #FFA500,
                0 0 20px #FF8C00;
            color: #FFD700;
        }}
        to {{
            text-shadow:
                0 0 10px #FFFACD,
                0 0 15px #FFA500,
                0 0 30px #FF4500;
            color: #FFFACD;
        }}
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
            font-size: 1.4rem;
            padding-top: 30px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">🐾 Dubzzz_Valo\'s Streaming Hub</div>', unsafe_allow_html=True)

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
        Thanks for stopping by! Follow for more awesome streams 🙏✨
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
