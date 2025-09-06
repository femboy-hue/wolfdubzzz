import streamlit as st

st.set_page_config(layout="wide")

# CSS Styles
st.markdown("""
<style>
/* Background starry sky on right half */
body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #0b0c10;
    color: #fff;
    overflow-x: hidden;
}

.main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 0 5vw;
}

/* Container for left (links + title) and right (images) */
.container {
    display: flex;
    width: 100%;
    max-width: 1200px;
}

/* Left side: title + links + footer */
.left {
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Title styling */
.title {
    font-size: 3rem;
    font-weight: 900;
    color: #ff4d4d;
    text-align: center;
    margin-bottom: 40px;
}

/* Social links container */
.links {
    display: flex;
    flex-direction: column;
    gap: 25px;
    align-items: flex-start;
}

a {
    color: #4da6ff;
    font-weight: bold;
    font-size: 1.25rem;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: color 0.3s, transform 0.3s;
}

a:hover {
    color: #ff6666;
    transform: scale(1.05);
    cursor: pointer;
}

/* Footer text */
.footer {
    font-style: italic;
    font-size: 1rem;
    color: #bbb;
    text-align: center;
    margin-top: 40px;
}

/* Right side: images */
.right {
    flex: 1;
    position: relative;
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
}

/* Starry night background */
.star-bg {
    position: absolute;
    top: 0;
    right: 0;
    width: 60vw;
    height: 100vh;
    background: url('https://i.ibb.co/4NSwMMQ/star-night-bg.png') no-repeat center center;
    background-size: cover;
    z-index: 0;
    filter: brightness(0.8);
    border-radius: 0 0 0 40px;
}

/* Cat image - top right, center vertically */
.cat {
    position: relative;
    width: 250px;
    height: auto;
    margin-top: 40px;
    z-index: 1;
    filter: drop-shadow(0 0 10px rgba(255, 102, 102, 0.7));
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
        align-items: center;
    }
    .right {
        width: 100%;
        justify-content: center;
        margin-top: 20px;
    }
    .star-bg {
        width: 100vw;
        height: 300px;
        border-radius: 40px 40px 0 0;
    }
    .cat {
        width: 150px;
        margin-top: 10px;
    }
    .title {
        font-size: 2.25rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="main">
  <div class="container">
    <div class="left">
      <h1 class="title">🐾 Dubzzz_Valo's Streaming Hub 🌟</h1>
      <div class="links">
        <a href="https://youtube.com" target="_blank">🎥 YouTube</a>
        <a href="https://instagram.com" target="_blank">📸 Instagram</a>
        <a href="https://tiktok.com" target="_blank">🎵 TikTok</a>
        <a href="https://twitch.tv" target="_blank">🎮 Twitch</a>
      </div>
      <div class="footer">Thanks for stopping by! Follow for more content 🙏</div>
    </div>
    <div class="right">
      <div class="star-bg"></div>
      <img src="https://i.ibb.co/pjDxxcM/cat-image.png" class="cat" alt="Cat"/>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
