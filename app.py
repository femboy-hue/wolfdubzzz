import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="wide")

# CSS for full screen background and styling
css = """
<style>
/* Make body and main fill the screen and remove padding */
[data-testid="stAppViewContainer"] > .main {
    padding: 0 !important;
    height: 100vh;
    overflow: hidden;
    position: relative;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
}

/* Full screen background image */
.background-image {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('/file=starry_sky.png');
    background-size: cover;
    background-position: center;
    z-index: -1;
    filter: brightness(0.6);
}

/* Overlay container to center content */
.content {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 50px;
    height: 100vh;
    justify-content: flex-start;
    gap: 25px;
}

/* Cat profile pic */
.profile-pic {
    width: 180px;
    height: 180px;
    border-radius: 90px;
    border: 4px solid #ee0979;
    box-shadow: 0 0 20px 5px #ff6a00;
}

/* Title styling with gradient */
.title {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    text-align: center;
}

/* Links container */
.links {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
    justify-content: center;
}

/* Each link styling */
.link-item {
    font-size: 20px;
    color: #ee0979;
    font-weight: 700;
    text-decoration: none;
    padding: 12px 25px;
    border-radius: 30px;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 10px;
    user-select: none;
}

.link-item:hover {
    color: #ff6a00;
    border: 2px solid #ff6a00;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    box-shadow: 0 0 15px #ff6a00;
    cursor: pointer;
}

/* Footer at bottom */
.footer {
    position: fixed;
    bottom: 15px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    color: #bbb;
    font-style: italic;
    font-weight: 600;
    padding: 0 40px;
    user-select: none;
    font-size: 16px;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Background div
st.markdown('<div class="background-image"></div>', unsafe_allow_html=True)

# Content container
st.markdown('<div class="content">', unsafe_allow_html=True)

# Cat profile pic (use width to size)
st.image("cat.png", use_column_width=False, width=180, output_format="PNG", clamp=False)

# Title
st.markdown('<h1 class="title">✨ Dubzzz_Valo\'s Streaming Hub ✨</h1>', unsafe_allow_html=True)

# Social Links
st.markdown('<div class="links">', unsafe_allow_html=True)

links = [
    ("🎥 YouTube", "https://www.youtube.com/"),
    ("📸 Instagram", "https://www.instagram.com/"),
    ("🎵 TikTok", "https://www.tiktok.com/"),
    ("🎮 Twitch", "https://www.twitch.tv/"),
]

for text, url in links:
    st.markdown(f'<a class="link-item" href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer fixed at bottom
footer_html = """
<div class="footer">
    <div>Thanks for visiting! 🙏</div>
    <div>I hope you follow everything and enjoy my content! 💖</div>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
