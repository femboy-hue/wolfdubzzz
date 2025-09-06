import streamlit as st

# Page config for wide layout
st.set_page_config(layout="wide")

# Paths to your images
star_bg_path = "/mnt/data/starry_sky.png"
cat_img_path = "/mnt/data/cat.png"

st.markdown(f"""
<style>
/* Reset */
body, html {{
  margin: 0; padding: 0; height: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: url("file://{star_bg_path}") no-repeat center center fixed;
  background-size: cover;
  color: white;
  overflow-x: hidden;
}}

/* Container fills viewport */
.container {{
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  backdrop-filter: brightness(0.7);
}}

/* Title at top center */
.title {{
  font-size: 3rem;
  font-weight: 900;
  margin-top: 30px;
  text-align: center;
  color: #ff4d4d;
  text-shadow: 0 0 5px #ff4d4d;
}}

/* Cat image centered and medium sized */
.cat {{
  max-width: 250px;
  width: 100%;
  margin: auto;
  filter: drop-shadow(0 0 10px rgba(255, 77, 77, 0.8));
  display: block;
}}

/* Links container under cat */
.links {{
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  margin-bottom: 40px;
}}

/* Link styling */
.links a {{
  color: #4da6ff;
  font-weight: 700;
  font-size: 1.3rem;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: color 0.3s ease, transform 0.3s ease;
}}

.links a:hover {{
  color: #ff6666;
  transform: scale(1.1);
  cursor: pointer;
  text-decoration: underline;
}}

/* Footer text */
.footer {{
  font-size: 1.1rem;
  font-style: italic;
  margin-bottom: 10px;
  color: #bbb;
  text-align: center;
}}

/* Responsive adjustments */
@media (max-width: 768px) {{
  .title {{
    font-size: 2.2rem;
  }}
  .cat {{
    max-width: 180px;
  }}
  .links a {{
    font-size: 1.1rem;
  }}
}}
</style>

<div class="container">
  <h1 class="title">🐾 Dubzzz_Valo's Streaming Hub 🌟</h1>
  
  <img src="file://{cat_img_path}" alt="Cat" class="cat" />
  
  <div class="links">
    <a href="https://youtube.com" target="_blank">🎥 YouTube</a>
    <a href="https://instagram.com" target="_blank">📸 Instagram</a>
    <a href="https://tiktok.com" target="_blank">🎵 TikTok</a>
    <a href="https://twitch.tv" target="_blank">🎮 Twitch</a>
  </div>
  
  <div class="footer">Thanks for stopping by! Follow for more content 🙏</div>
</div>
""", unsafe_allow_html=True)
