import streamlit as st
import base64

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", page_icon="🌌", layout="wide")

st.markdown(
    """
    <style>
    /* Reset margin/padding */
    body, html, #root, .main {
        margin: 0; padding: 0; height: 100%; width: 100%; overflow-x: hidden;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #000; color: #fff;
    }

    /* Starry background full screen */
    .starry-bg {
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url("data:image/png;base64,{starry_img_base64}");
        background-size: cover;
        background-position: center;
        filter: brightness(0.7);
        z-index: -1;
    }

    /* Container centers content and adds padding */
    .container {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem 1rem 4rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Title styling */
    .title {
        font-size: 3rem;
        font-weight: 900;
        color: #ff6f3c;
        text-shadow: 0 0 8px #ff6f3c, 0 0 20px #ff6f3c;
        user-select: none;
    }

    /* Sparkle emoji next to title */
    .sparkle {
        font-size: 3rem;
        margin-left: 10px;
        animation: sparkleAnim 2s infinite;
    }
    @keyframes sparkleAnim {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.3); }
    }

    /* Tagline below title */
    .tagline {
        font-style: italic;
        margin-top: 0.4rem;
        margin-bottom: 2rem;
        font-size: 1.3rem;
        color: #f1a661cc;
    }

    /* Cat image styling */
    .cat-img {
        width: 180px;
        height: auto;
        border-radius: 50%;
        border: 4px solid #ff6f3c;
        box-shadow: 0 0 20px #ff6f3caa;
        margin-bottom: 2rem;
        user-select: none;
    }

    /* Links container */
    .links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 3rem;
        flex-wrap: wrap;
    }

    /* Each link styling */
    .links a {
        color: #f1a661dd;
        font-size: 1.2rem;
        text-decoration: none;
        font-weight: 600;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        transition: all 0.3s ease;
        user-select: none;
        box-shadow: 0 0 10px #f1a66166;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(255, 111, 60, 0.2);
    }
    .links a:hover {
        color: #ff6f3c;
        background: rgba(255, 111, 60, 0.5);
        box-shadow: 0 0 20px #ff6f3ccc;
        transform: scale(1.1);
    }

    /* Footer text styling */
    .footer {
        font-size: 1.1rem;
        color: #ff6f3caa;
        font-style: italic;
        user-select: none;
        text-shadow: 0 0 6px #ff6f3c88;
    }

    /* Responsive */
    @media (max-width: 600px) {
        .title {
            font-size: 2rem;
        }
        .cat-img {
            width: 140px;
        }
        .links a {
            font-size: 1rem;
            padding: 0.4rem 0.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Image uploaders ---
starry_img = st.file_uploader("Upload the starry sky background image (starry_sky.png)", type=["png", "jpg"])
cat_img = st.file_uploader("Upload the cat profile picture (cat.png)", type=["png", "jpg"])

def img_to_base64(img_file):
    return base64.b64encode(img_file.read()).decode()

if starry_img and cat_img:
    starry_img_base64 = img_to_base64(starry_img)
    cat_img_base64 = img_to_base64(cat_img)

    # Now inject the base64 into CSS and HTML by rerunning markdown with correct image data

    page_html = f"""
    <div class="starry-bg"></div>
    <div class="container">
        <div>
            <span class="title">Dubzzz_Valo’s Streaming Galaxy</span><span class="sparkle">✨</span>
        </div>
        <div class="tagline">Your Gateway to Epic Plays!</div>

        <img src="data:image/png;base64,{cat_img_base64}" alt="Cat" class="cat-img" />

        <div class="links">
            <a href="https://youtube.com" target="_blank">🎥 YouTube</a>
            <a href="https://instagram.com" target="_blank">📸 Instagram</a>
            <a href="https://tiktok.com" target="_blank">🎵 TikTok</a>
            <a href="https://twitch.tv" target="_blank">🎮 Twitch</a>
        </div>

        <div class="footer">
            Thanks for dropping by — don’t forget to hit that follow! <span>🙌</span>
        </div>
    </div>
    """

    # Display the page HTML
    st.markdown(page_html, unsafe_allow_html=True)

else:
    st.info("Please upload **both** images above to load the streaming page.")
