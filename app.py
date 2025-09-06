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
paw_print_img = Image.open("/mnt/data/854afe68-f53e-4fda-845b-e794b8dfd5ab.png")

background_base64 = img_to_base64(background_img)
paw_print_base64 = img_to_base64(paw_print_img)

st.markdown(
    f"""
    <style>
    /* Starfield background animation */
    body, .stApp {{
        margin: 0; padding: 0; height: 100vh;
        background: black url("data:image/png;base64,{background_base64}") repeat;
        background-size: cover;
        overflow: hidden;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #0ff;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* Starfield animation overlay */
    @keyframes starMove {{
        from {{ background-position: 0 0; }}
        to {{ background-position: 10000px 0; }}
    }}
    .starfield {{
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: black url("https://i.imgur.com/88bT3c9.png") repeat;
        background-size: 150px 150px;
        animation: starMove 150s linear infinite;
        z-index: -2;
        pointer-events: none;
    }}

    /* Floating paw prints animation */
    @keyframes floatUp {{
        0% {{
            transform: translateY(100vh) translateX(0);
            opacity: 0;
        }}
        10% {{
            opacity: 1;
        }}
        100% {{
            transform: translateY(-10vh) translateX(30px);
            opacity: 0;
        }}
    }}

    .paw-floating {{
        position: fixed;
        bottom: -10vh;
        width: 40px;
        height: 40px;
        background-image: url("data:image/png;base64,{paw_print_base64}");
        background-size: contain;
        background-repeat: no-repeat;
        opacity: 0.7;
        animation: floatUp 20s linear infinite;
        filter: drop-shadow(0 0 4px #00ffff);
        z-index: -1;
        user-select: none;
    }}

    .paw1 {{
        left: 10vw;
        animation-delay: 0s;
    }}
    .paw2 {{
        left: 30vw;
        animation-delay: 7s;
        animation-duration: 22s;
        opacity: 0.5;
    }}
    .paw3 {{
        left: 70vw;
        animation-delay: 15s;
        animation-duration: 25s;
    }}
    .paw4 {{
        left: 85vw;
        animation-delay: 10s;
        animation-duration: 20s;
        opacity: 0.6;
    }}

    /* Neon flicker title */
    @keyframes neon-flicker {{
        0%, 100% {{
            text-shadow:
                0 0 5px #00ffff,
                0 0 10px #00ffff,
                0 0 20px #00ffff,
                0 0 40px #0ff,
                0 0 80px #0ff,
                0 0 90px #0ff,
                0 0 100px #0ff,
                0 0 150px #0ff;
            color: #0ff;
        }}
        50% {{
            text-shadow:
                0 0 2px #00ffff,
                0 0 5px #00ffff,
                0 0 10px #00ffff,
                0 0 20px #0ff;
            color: #a0ffff;
        }}
    }}

    /* Footer color cycling glow */
    @keyframes footerGlow {{
        0% {{ color: #0ff; text-shadow: 0 0 10px #0ff; }}
        50% {{ color: #00bfff; text-shadow: 0 0 20px #00bfff; }}
        100% {{ color: #0ff; text-shadow: 0 0 10px #0ff; }}
    }}

    /* Fade in footer */
    @keyframes fadeGlow {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}

    .container {{
        text-align: center;
        max-width: 800px;
        padding: 20px;
        position: relative;
        z-index: 1;
    }}

    .title {{
        font-size: 3.5rem;
        font-weight: 900;
        text-transform: uppercase;
        animation: neon-flicker 2.5s infinite alternate;
        margin-bottom: 1rem;
        letter-spacing: 0.1em;
        user-select: none;
    }}

    .tagline {{
        font-style: italic;
        font-size: 1.3rem;
        color: #33ffff;
        margin-bottom: 2rem;
        text-shadow: 0 0 6px #33ffff;
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
        text-shadow: 0 0 15px #00ffff;
        background-color: rgba(0, 255, 255, 0.15);
        transform: scale(1.1);
        color: #00ffff;
    }}

    .footer {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-style: italic;
        font-size: 1.5rem;
        color: #0ff;
        animation: footerGlow 5s ease-in-out infinite, fadeGlow 3s ease forwards;
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

    <div class="starfield"></div>
    <div class="paw-floating paw1"></div>
    <div class="paw-floating paw2"></div>
    <div class="paw-floating paw3"></div>
    <div class="paw-floating paw4"></div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">🐾 DUBZZZ_VALO\'S STREAMING HUB</div>', unsafe_allow_html=True)

st.markdown('<div class="tagline">Where Epic Streams Meet Cozy Vibes</div>', unsafe_allow_html=True)

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
