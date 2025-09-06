import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="wide")

# CSS for full background and layout
st.markdown(
    """
    <style>
    /* Full screen background with starry sky */
    .stApp {
        background-image: url('/file=d06d0e8c-1389-491f-82cb-adfcdb3ff456.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: start;
        padding-top: 60px;
        position: relative;
    }

    /* Cat profile picture */
    .profile-pic {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #ee0979;
        box-shadow: 0 0 15px 5px #ff6a00;
        object-fit: cover;
        margin-bottom: 25px;
    }

    /* Title style */
    .title {
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 40px 0;
        text-align: center;
    }

    /* Social links container */
    .links {
        display: flex;
        gap: 40px;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 40px;
    }

    /* Each social link style */
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

    /* Footer fixed at bottom left and right */
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
    """,
    unsafe_allow_html=True,
)

# Cat profile pic centered top
st.markdown('<img src="/file=cat.png" class="profile-pic" alt="Profile Pic">', unsafe_allow_html=True)

# Title centered below cat
st.markdown('<h1 class="title">✨ Dubzzz_Valo\'s Streaming Hub ✨</h1>', unsafe_allow_html=True)

# Social links centered
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

# Footer fixed left and right bottom
footer_html = """
<div class="footer">
    <div>Thanks for visiting! 🙏</div>
    <div>I hope you follow everything and enjoy my content! 💖</div>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
