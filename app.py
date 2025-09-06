import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="wide")

# CSS to style the full background, profile pic, title, links, footer
st.markdown("""
<style>
/* Full screen background with starry sky */
.stApp {
    background-image: url('/file=d06d0e8c-1389-491f-82cb-adfcdb3ff456.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    min-height: 100vh;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 60px;
    position: relative;
}

/* Profile picture centered and bigger */
.profile-pic {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 4px solid #ee0979;
    box-shadow: 0 0 20px 8px #ff6a00;
    object-fit: cover;
    margin-bottom: 40px;
}

/* Title style */
.title {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 40px;
    text-align: center;
}

/* Social links container - horizontal and centered */
.links {
    display: flex;
    gap: 50px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 60px;
}

/* Individual link styling */
.link-item {
    font-size: 22px;
    color: #ee0979;
    font-weight: 700;
    text-decoration: none;
    padding: 14px 30px;
    border-radius: 30px;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 10px;
}

.link-item:hover {
    color: #ff6a00;
    border: 2px solid #ff6a00;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    box-shadow: 0 0 20px #ff6a00;
    cursor: pointer;
}

/* Footer fixed bottom left and right */
.footer {
    position: fixed;
    bottom: 10px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    color: #bbb;
    font-style: italic;
    font-weight: 600;
    padding: 0 40px;
    user-select: none;
    font-size: 16px;
    pointer-events: none;
}
</style>
""", unsafe_allow_html=True)

# Profile picture (using uploaded cat image)
st.markdown('<img src="/file=46b6af7e-f148-439e-8aa8-a79deb61aaa2.png" class="profile-pic" alt="Profile Pic">', unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">✨ Dubzzz_Valo\'s Streaming Hub ✨</h1>', unsafe_allow_html=True)

# Social Links horizontally aligned and centered
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

# Footer fixed bottom left and right
footer_html = """
<div class="footer">
    <div>Thanks for visiting! 🙏</div>
    <div>I hope you follow everything and enjoy my content! 💖</div>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
