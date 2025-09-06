import streamlit as st
import base64

st.set_page_config(page_title="Dubzzz_Valo's Streaming Realm", page_icon="✨", layout="centered")

# Load your uploaded images as base64 (replace these with your actual base64 strings)
with open("/mnt/data/bcb3a55a-5a8d-46dc-9a92-f433f4b44bcc.png", "rb") as f:
    starry_bg_b64 = base64.b64encode(f.read()).decode()

with open("/mnt/data/2f8196b1-f2a8-4d2e-906c-83bca319fe8d.png", "rb") as f:
    cat_img_b64 = base64.b64encode(f.read()).decode()

# CSS Styling with embedded images and custom fonts
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');

    .stApp {{
        background: url("data:image/png;base64,{starry_bg_b64}") no-repeat center center fixed;
        background-size: cover;
        color: #f0e8e8;
        font-family: 'Poppins', sans-serif;
        overflow-x: hidden;
        min-height: 100vh;
        padding: 40px 20px;
        text-align: center;
    }}

    /* Title with glowing effect and underline */
    .title {{
        font-size: 3rem;
        font-weight: 800;
        color: #ffa500;
        text-shadow:
            0 0 7px #ffa500,
            0 0 20px #ff6f00,
            0 0 30px #ff6f00;
        border-bottom: 4px solid #ff6f00;
        display: inline-block;
        padding-bottom: 10px;
        margin-bottom: 40px;
        user-select: none;
        letter-spacing: 2px;
    }}

    /* Cat image */
    .cat-img {{
        display: block;
        margin: 0 auto 50px auto;
        width: 240px;
        border-radius: 20px;
        box-shadow: 0 0 25px 8px rgba(255, 111, 0, 0.75);
        transition: transform 0.3s ease;
    }}

    .cat-img:hover {{
        transform: scale(1.1);
    }}

    /* Social links container */
    .social-links {{
        display: flex;
        justify-content: center;
        gap: 50px;
        font-size: 1.3rem;
        font-weight: 600;
        color: #d7d7d7;
        user-select: none;
        margin-bottom: 70px;
    }}

    .social-links a {{
        color: #d7d7d7;
        text-decoration: none;
        transition: color 0.3s ease;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .social-links a:hover {{
        color: #ffa500;
        text-shadow: 0 0 10px #ff8c00;
        cursor: pointer;
    }}

    /* Footer text */
    .footer {{
        font-style: italic;
        font-size: 1.1rem;
        color: #ffb84d;
        text-shadow: 0 0 10px #ff8c00;
        user-select: none;
        margin-top: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<h1 class="title">Dubzzz_Valo\'s Streaming Realm — Enter the Purrfect Stream!</h1>', unsafe_allow_html=True)

# Cat image
st.markdown(
    f'<img class="cat-img" src="data:image/png;base64,{cat_img_b64}" alt="Cat profile picture">',
    unsafe_allow_html=True,
)

# Social media links with emojis as icons
st.markdown(
    """
    <div class="social-links">
        <a href="https://www.youtube.com/" target="_blank">🎥 <strong>YouTube</strong></a>
        <a href="https://www.instagram.com/" target="_blank">📸 <strong>Instagram</strong></a>
        <a href="https://www.tiktok.com/" target="_blank">🎵 <strong>TikTok</strong></a>
        <a href="https://www.twitch.tv/" target="_blank">🎮 <strong>Twitch</strong></a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <div class="footer">
        Thanks for swinging by! Catch you soon for more epic streams. 🙏🔥
    </div>
    """,
    unsafe_allow_html=True,
)
