import streamlit as st
import base64

st.set_page_config(page_title="Dubzzz_Valo's Streaming Realm", page_icon="✨", layout="centered")

# Helper function to encode images to base64 for CSS backgrounds
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Upload widgets to upload your images
st.markdown("### Upload the starry sky background image (starry_sky.png)")
starry_sky_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="starry")
st.markdown("### Upload the cat profile picture (cat.png)")
cat_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="cat")

if starry_sky_file and cat_file:
    # Convert uploaded files to base64
    starry_img_base64 = base64.b64encode(starry_sky_file.read()).decode()
    cat_img_base64 = base64.b64encode(cat_file.read()).decode()

    # Main CSS styling and animation
    st.markdown(
        f"""
        <style>
        /* Background starry sky */
        .stApp {{
            background: url("data:image/png;base64,{starry_img_base64}") no-repeat center center fixed;
            background-size: cover;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow-x: hidden;
        }}

        /* Title styling */
        .title {{
            font-size: 2.8rem;
            font-weight: 800;
            color: #FF6F00;
            text-align: center;
            text-shadow:
                0 0 5px #FF6F00,
                0 0 10px #FF6F00,
                0 0 20px #FF6F00;
            border-bottom: 3px solid #FF6F00;
            width: fit-content;
            margin: 0 auto 30px auto;
            padding-bottom: 8px;
            user-select: none;
        }}

        /* Centered cat image with shadow */
        .cat-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 15px;
            width: 220px;
            box-shadow: 0 0 15px rgba(255, 111, 0, 0.8);
            margin-bottom: 40px;
        }}

        /* Social media container */
        .social-links {{
            display: flex;
            justify-content: center;
            gap: 40px;
            font-weight: 600;
            font-size: 1.2rem;
            margin-bottom: 60px;
            user-select: none;
        }}

        .social-links a {{
            text-decoration: none;
            color: #b0c4de;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .social-links a:hover {{
            color: #FF6F00;
            text-shadow: 0 0 8px #FF6F00;
            cursor: pointer;
        }}

        /* Footer styling */
        .footer {{
            font-style: italic;
            font-size: 1rem;
            color: #e0e0e0;
            text-align: center;
            margin-top: 40px;
            text-shadow: 0 0 6px rgba(255, 255, 255, 0.5);
            user-select: none;
        }}

        /* Floating stars animation */
        @keyframes floatStars {{
            0% {{
                transform: translateY(0);
            }}
            50% {{
                transform: translateY(-10px);
            }}
            100% {{
                transform: translateY(0);
            }}
        }}

        .star {{
            position: fixed;
            background: white;
            border-radius: 50%;
            opacity: 0.8;
            animation: floatStars 4s ease-in-out infinite;
            pointer-events: none;
        }}

        .star:nth-child(1) {{
            width: 4px;
            height: 4px;
            top: 15%;
            left: 10%;
            animation-delay: 0s;
        }}
        .star:nth-child(2) {{
            width: 3px;
            height: 3px;
            top: 40%;
            left: 30%;
            animation-delay: 1.5s;
        }}
        .star:nth-child(3) {{
            width: 5px;
            height: 5px;
            top: 70%;
            left: 50%;
            animation-delay: 3s;
        }}
        .star:nth-child(4) {{
            width: 3px;
            height: 3px;
            top: 80%;
            left: 70%;
            animation-delay: 4.5s;
        }}
        .star:nth-child(5) {{
            width: 4px;
            height: 4px;
            top: 20%;
            left: 80%;
            animation-delay: 6s;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Stars decoration elements
    for _ in range(5):
        st.markdown('<div class="star"></div>', unsafe_allow_html=True)

    # Title
    st.markdown('<h1 class="title">Dubzzz_Valo\'s Streaming Realm — Enter the Purrfect Stream!</h1>', unsafe_allow_html=True)

    # Cat image centered
    st.markdown(
        f'<img class="cat-img" src="data:image/png;base64,{cat_img_base64}" alt="Cat profile picture"/>',
        unsafe_allow_html=True,
    )

    # Social media links with icons
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

    # Footer text with call to action
    st.markdown(
        """
        <div class="footer">
            Thanks for stopping by! Follow for more content 🙏
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("Please upload both images above to load the streaming page.")
