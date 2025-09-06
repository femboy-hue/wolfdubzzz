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
cat_base64 = img_to_base64(cat_img)

# CSS styles with merged improvements
st.markdown(
    f"""
    <style>
    /* Background */
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
        max-width: 800px;
        text-align: center;
        padding: 20px;
        position: relative;
        z-index: 2;
    }}

    /* Emoji bar inline with title */
    .emoji-bar {{
        display: inline-flex;
        gap: 12px;
        font-size: 1.8rem;
        margin-bottom: 12px;
        filter: drop-shadow(0 0 4px #00ffff);
        vertical-align: middle;
        justify-content: center;
        width: 100%;
    }}

    /* Title */
    .title {{
        font-size: 2.2rem;
        font-weight: 900;
        color: #00f9ff;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #00f9ff, 0 0 30px #00f9ff;
        margin: 0 auto 12px auto;
        max-width: 90%;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.2;
    }}

    /* Subtitle */
    .tagline {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 1.7rem;
        font-weight: 600;
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff, 0 0 20px #00ffff;
        margin: 0 auto 30px auto;
        max-width: 90%;
        white-space: nowrap;
    }}

    /* Cat Image */
    .cat-img {{
        width: 300px !important;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6);
        margin: 0 auto 3rem auto;
        transition: transform 0.3s ease;
        display: block;
        position: relative;
        z-index: 2;
    }}

    .cat-img:hover {{
        transform: scale(1.05);
    }}

    /* Footer */
    .footer {{
        font-style: italic;
        font-size: 1.4rem;
        color: #00ffff;
        padding-top: 20px;
        text-shadow: 0 0 15px #00ffff;
        position: relative;
        z-index: 2;
    }}

    /* Responsive */
    @media (max-width: 600px) {{
        .emoji-bar {{
            font-size: 1.4rem;
            gap: 8px;
        }}
        .title {{
            font-size: 1.8rem;
            white-space: normal;
        }}
        .tagline {{
            font-size: 1.3rem;
            white-space: normal;
            margin-bottom: 20px;
        }}
        .cat-img {{
            width: 80vw !important;
            margin-bottom: 1.5rem;
        }}
        .footer {{
            font-size: 1.2rem;
            padding-top: 15px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Container for all content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Emoji bar inline with title
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

# Title text
st.markdown(
    """
    <div class="title">DUBZZZ_VALO'S STREAMING HUB</div>
    """,
    unsafe_allow_html=True,
)

# Subtitle text with sparkle emoji
st.markdown(
    """
    <div class="tagline">Where Every Stream is Legendary ✨</div>
    """,
    unsafe_allow_html=True,
)

# Cat image with CSS styling (using base64 embedded img tag)
st.markdown(
    f'<img src="data:image/png;base64,{cat_base64}" class="cat-img" alt="Cat Image" />',
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <div class="footer">© 2025 DUBZZZ_VALO. All Rights Reserved.</div>
    """,
    unsafe_allow_html=True,
)

# Close container div
st.markdown('</div>', unsafe_allow_html=True)
