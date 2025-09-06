import streamlit as st
from PIL import Image

# Load images
cat_img = Image.open("cat.png")
starry_img = Image.open("starry_sky.png")

# Inject CSS for full background image and centering cat image
st.markdown(
    f"""
    <style>
    /* Full screen starry sky background */
    .stApp {{
        background-image: url("data:image/png;base64,{starry_img_to_base64(starry_img)}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Container for centering cat and text */
    .center-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        color: white;
        text-align: center;
    }}

    /* Title style */
    .title {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF4500;
        text-shadow: 2px 2px 4px black;
        margin-bottom: 1rem;
    }}

    /* Links style */
    .links a {{
        color: #87CEFA;
        margin: 0 15px;
        font-size: 1.2rem;
        text-decoration: none;
    }}

    .footer {{
        font-style: italic;
        margin-top: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# Helper function to convert image to base64
def starry_img_to_base64(img):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode()

# Title and cat image centered
st.markdown(
    """
    <div class="center-container">
        <div class="title">🐾 Dubzzz_Valo's Streaming Hub 🌟</div>
    """,
    unsafe_allow_html=True,
)

st.image(cat_img, width=250, caption="Cat", output_format="PNG")

# Links below cat image
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
    </div>
    """,
    unsafe_allow_html=True,
)
