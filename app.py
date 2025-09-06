import streamlit as st
from PIL import Image

# Set page config (optional)
st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="centered")

# Title
st.markdown(
    """
    <h1 style='text-align:center; color:#FF4500; text-shadow: 2px 2px 4px #000000;'>
        🐾 Dubzzz_Valo's Streaming Hub 🌟
    </h1>
    """,
    unsafe_allow_html=True,
)

# Load images
cat_img = Image.open("cat.png")
starry_img = Image.open("starry_sky.png")

# Show cat image centered and medium sized
st.image(cat_img, width=250, caption="Cat")

# Show starry sky below cat centered and a bit bigger
st.image(starry_img, width=400, caption="Starry Sky")

# Social Links (centered)
st.markdown(
    """
    <div style='text-align:center; font-size:18px; margin-top:30px;'>
        🎥 <a href="https://youtube.com" target="_blank">YouTube</a> &nbsp;&nbsp;&nbsp;
        📸 <a href="https://instagram.com" target="_blank">Instagram</a> &nbsp;&nbsp;&nbsp;
        🎵 <a href="https://tiktok.com" target="_blank">TikTok</a> &nbsp;&nbsp;&nbsp;
        🎮 <a href="https://twitch.tv" target="_blank">Twitch</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer message
st.markdown(
    """
    <p style='text-align:center; font-style: italic; margin-top: 40px;'>
        Thanks for stopping by! Follow for more content 🙏
    </p>
    """,
    unsafe_allow_html=True,
)
