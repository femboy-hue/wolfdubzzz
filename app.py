import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load new cat image - use full path to avoid FileNotFoundError
cat_img = Image.open("/mnt/data/6ad72f1d-0624-4cc8-b781-29bf5e3a9685.png")
background_img = Image.open("skye.png")
background_base64 = img_to_base64(background_img)

st.markdown(
    f"""
    <style>
    @keyframes floatUp {{
        0% {{
            transform: translateY(0) translateX(0);
            opacity: 1;
        }}
        100% {{
            transform: translateY(-100px) translateX(20px);
            opacity: 0;
        }}
    }}

    @keyframes floatSide {{
        0% {{
            transform: translateX(0);
            opacity: 1;
        }}
        50% {{
            transform: translateX(10px);
        }}
        100% {{
            transform: translateX(0);
            opacity: 1;
        }}
    }}

    @keyframes glowCycle {{
        0%, 100% {{
            text-shadow: 0 0 8px #00f9ff, 0 0 20px #00f9ff;
            color: #00f9ff;
        }}
        50% {{
            text-shadow: 0 0 20px #ff007f, 0 0 40px #ff007f;
            color: #ff007f;
        }}
    }}

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
        overflow: hidden;
        position: relative;
    }}

    .container {{
        text-align: center;
        max-width: 800px;
        padding: 20px;
        position: relative;
        z-index: 2;
    }}

    /* Emoji container above title */
    .emoji-bar {{
        display: flex;
        justify-content: center;
        gap: 20px;
        font-size: 2rem;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 4px #00ffff);
    }}

    .title {{
        font-size: 2.4rem;
        font-weight: 900;
        color: #00f9ff;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow: 0 0 10px #00f9ff, 0 0 30px #00f9ff;
        margin-bottom: 0.3rem;
        display: inline-block;
        position: relative;
        z-index: 3;
    }}

    .title-emoji {{
        margin: 0 6px;
        filter: drop-shadow(0 0 6px #ff0080);
    }}

    .tagline {{
        font-family: 'Brush Script MT', cursive;
        font-size: 1.6rem;
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff, 0 0 20px #00ffff;
        margin-top: 5px;
        margin-bottom: 1.8rem;
        white-space: nowrap;
    }}

    .cat-img {{
        width: 300px !important;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6);
        margin-bottom: 2.5rem;
        transition: transform 0.3s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        z-index: 2;
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
        color: #00f9ff;
        text-shadow: 0 0 6px #00f9ff;
        position: relative;
        z-index: 2;
    }}

    .links a {{
        color: #00f9ff;
        text-decoration: none;
        padding: 8px 12px;
        border-radius: 6px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 6px;
        font-weight: 700;
        font-size: 1.2rem;
    }}

    .links a:hover {{
        text-shadow: 0 0 10px #ff00aa;
        color: #ff00aa;
        transform: scale(1.1);
    }}

    .footer {{
        font-style: italic;
        font-size: 1.6rem;
        color: #00ffff;
        padding-top: 20px;
        animation: glowCycle 5s ease-in-out infinite;
        text-shadow: 0 0 15px #00ffff;
        position: relative;
        z-index: 2;
    }}

    /* Floating emojis container */
    .floating-icons {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: visible;
    }}

    /* Individual floating emoji styles with different animations and delays */
    .floating-icons span {{
        position: absolute;
        font-size: 1.5rem;
        opacity: 0.8;
        user-select: none;
        filter: drop-shadow(0 0 2px #00ffff);
        animation-timing-function: ease-in-out;
    }}

    .star {{
        color: #fffacd;
        animation: floatUp 10s linear infinite;
    }}

    .heart {{
        color: #ff4081;
        animation: floatSide 8s ease-in-out infinite;
    }}

    .play {{
        color: #00ffea;
        animation: floatUp 12s linear infinite;
    }}

    .bolt {{
        color: #ffff00;
        animation: floatSide 7s ease-in-out infinite;
    }}

    /* Different delays and starting positions */
    .floating-icons span:nth-child(1) {{
        top: 90%;
        left: 20%;
        animation-delay: 0s;
        font-size: 1.8rem;
    }}
    .floating-icons span:nth-child(2) {{
        top: 80%;
        left: 50%;
        animation-delay: 3s;
        font-size: 2rem;
    }}
    .floating-icons span:nth-child(3) {{
        top: 85%;
        left: 70%;
        animation-delay: 6s;
        font-size: 1.6rem;
    }}
    .floating-icons span:nth-child(4) {{
        top: 90%;
        left: 35%;
        animation-delay: 9s;
        font-size: 1.7rem;
    }}
    .floating-icons span:nth-child(5) {{
        top: 75%;
        left: 60%;
        animation-delay: 1.5s;
        font-size: 1.5rem;
    }}
    .floating-icons span:nth-child(6) {{
        top: 80%;
        left: 40%;
        animation-delay: 4.5s;
        font-size: 1.9rem;
    }}

    /* Responsive */
    @media (max-width: 600px) {{
        .emoji-bar {{
            font-size: 1.6rem;
            gap: 10px;
        }}
        .title {{
            font-size: 1.8rem;
            white-space: normal;
        }}
        .tagline {{
            font-size: 1.2rem;
            white-space: normal;
            margin-bottom: 1.2rem;
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

    <div class="floating-icons">
        <span class="star">✨</span>
        <span class="heart">💖</span>
        <span class="play">▶️</span>
        <span class="bolt">⚡</span>
        <span class="star">🌟</span>
        <span class="heart">💗</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)

# Emojis above title - consistent set (lightning, hearts, play)
st.markdown(
    """
    <div class="emoji-bar">
        <span>⚡</span>
        <span>❤️</span>
        <span>💔</span>
        <span>▶️</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Title with consistent emojis integrated and no line break
st.markdown(
    """
    <div class="title">
        ⚡ <span class="title-emoji">❤️</span> DUBZZZ_VALO'S STREAMING HUB <span class="title-emoji">💔</span> ⚡
    </div>
    """,
    unsafe_allow_html=True,
)

# Subtitle with neon glow, no background highlight, smaller font, closer spacing
st.markdown(
    """
    <div class="tagline">
        Where Every Stream is Legendary ✨
    </div>
    """,
    unsafe_allow_html=True,
)

# New cat image
st.markdown(f'<img src="data:image/png;base64,{img_to_base64(cat_img)}" class="cat-img" alt="Cat Image" />', unsafe_allow_html=True)

# Links row
st.markdown(
    """
    <div class="links">
        <a href="https://youtube.com" target="_blank">🎥 YouTube</a>
        <a href="https://instagram.com" target="_blank">📸 Instagram</a>
        <a href="https://tiktok.com" target="_blank">🎵 TikTok</a>
        <a href="https://twitch.tv" target="_blank">🎮 Twitch</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer with softer neon cyan glow color
st.markdown(
    """
    <div class="footer">
        Thanks for stopping by! Catch more epic streams soon 🙏✨
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
