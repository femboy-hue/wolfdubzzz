import streamlit as st
from PIL import Image

# Load images from your local /mnt/data folder
cat_img = Image.open("/mnt/data/cat.png")
star_bg_path = "/mnt/data/starry_sky.png"  # For CSS background, this needs a URL or base64 (see below)

# Set page config
st.set_page_config(layout="wide")

# Set starry sky as background via CSS with base64 encoding (see Option 2 below)

# Title
st.markdown("""
    <h1 style='
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        margin-top: 30px;
        color: #ff4d4d;
        text-shadow: 0 0 5px #ff4d4d;
    '>
    🐾 Dubzzz_Valo's Streaming Hub 🌟
    </h1>
    """, unsafe_allow_html=True)

# Center cat image with Streamlit image widget
st.image(cat_img, width=250, caption="Cat", output_format="PNG", use_column_width=False)

# Links with markdown and styling
st.markdown("""
    <div style="text-align: center; margin-top: 30px; font-size: 1.3rem; font-weight: 700;">
      <a href="https://youtube.com" style="color:#4da6ff; text-decoration:none; margin: 0 10px;">🎥 YouTube</a>
      <a href="https://instagram.com" style="color:#4da6ff; text-decoration:none; margin: 0 10px;">📸 Instagram</a>
      <a href="https://tiktok.com" style="color:#4da6ff; text-decoration:none; margin: 0 10px;">🎵 TikTok</a>
      <a href="https://twitch.tv" style="color:#4da6ff; text-decoration:none; margin: 0 10px;">🎮 Twitch</a>
    </div>
    <p style="text-align:center; margin-top: 40px; font-size: 1.1rem; color: #bbb; font-style: italic;">
      Thanks for stopping by! Follow for more content 🙏
    </p>
""", unsafe_allow_html=True)
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

starry_sky_base64 = get_base64_of_bin_file("/mnt/data/starry_sky.png")

background_css = f"""
<style>
body {{
  background-image: url("data:image/png;base64,{starry_sky_base64}");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}}
</style>
"""

st.markdown(background_css, unsafe_allow_html=True)
