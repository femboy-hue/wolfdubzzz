import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load images with correct filenames
cat_img = Image.open("cat.png")
background_img = Image.open("skye.png")
background_base64 = img_to_base64(background_img)

st.markdown(
    f"""
    <style>
    /* your existing styles here... */

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
        white-space: nowrap;  /* keep title on a single line */
    }}

    .title-emoji {{
        margin: 0 6px;
        filter: drop-shadow(0 0 6px #ff0080);
    }}

    /* rest of your styles ... */

    </style>

    <!-- Floating emojis and other styles remain unchanged -->
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)

# Remove the emoji bar above title as per sparing emojis or keep if you want.
# If you want to remove, comment out or delete the next block:
st.markdown(
    """
    <div class="emoji-bar" aria-label="Emojis">
        <span>⚡</span>
        <span>❤️</span>
        <span>💔</span>
        <span>▶️</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Simplified title with just two emojis sparingly placed at edges, no scattered emojis
st.markdown(
    """
    <div class="title">
        ⚡ <span class="title-emoji">❤️</span> DUBZZZ_VALO'S STREAMING HUB <span class="title-emoji">❤️</span> ⚡
    </div>
    """,
    unsafe_allow_html=True,
)

# Subtitle remains same
st.markdown(
    """
    <div class="tagline">
        Where Every Stream is Legendary ✨
    </div>
    """,
    unsafe_allow_html=True,
)

# Cat image
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

# Footer
st.markdown(
    """
    <div class="footer">
        Thanks for stopping by! Catch more epic streams soon 🙏✨
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
