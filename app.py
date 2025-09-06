import streamlit as st
import base64

# Load images and encode to base64
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

starry_img_base64 = img_to_base64("starry_sky.png")
cat_img_base64 = img_to_base64("cat.png")

# CSS + HTML
page_html = f"""
<style>
  /* Full screen background */
  body, html {{
    margin: 0; padding: 0; height: 100%;
    overflow-x: hidden;
  }}
  .starry-bg {{
    background-image: url("data:image/png;base64,{starry_img_base64}");
    background-size: cover;
    background-position: center;
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    filter: brightness(0.85);
  }}

  /* Container centered content */
  .container {{
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px 60px 20px;
    text-align: center;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }}

  /* Title */
  .title {{
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(90deg, #FF4500, #FFA500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
    white-space: nowrap;
    margin-bottom: 0.2rem;
    display: inline-block;
    vertical-align: middle;
  }}

  .sparkle {{
    animation: sparkleAnim 2.5s infinite;
    display: inline-block;
    font-size: 1.6rem;
    vertical-align: middle;
    margin-left: 6px;
  }}

  @keyframes sparkleAnim {{
    0%, 100% {{ opacity: 1; transform: rotate(0deg) scale(1); }}
    50% {{ opacity: 0.5; transform: rotate(20deg) scale(1.3); }}
  }}

  .tagline {{
    font-size: 1.2rem;
    font-style: italic;
    color: #FFD700;
    text-shadow: 0 0 6px #FFA500;
    margin-bottom: 30px;
  }}

  /* Cat Image */
  .cat-img {{
    width: 280px !important;
    border-radius: 20px;
    border: 4px solid #FF4500;
    box-shadow: 0 0 15px #FF4500, 0 0 30px #FFA500;
    margin: 0 auto 50px auto;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    display: block;
  }}

  .cat-img:hover {{
    box-shadow: 0 0 25px #FF4500, 0 0 50px #FFA500;
    transform: scale(1.1);
  }}

  /* Links */
  .links {{
    display: flex;
    justify-content: center;
    gap: 40px;
    font-size: 1.4rem;
    font-weight: 600;
    color: #87CEFA;
    text-shadow: 0 0 6px rgba(135, 206, 250, 0.8);
    margin-bottom: 3rem;
  }}

  .links a {{
    color: #87CEFA;
    text-decoration: none;
    padding: 10px 16px;
    border-radius: 8px;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .links a:hover {{
    text-decoration: underline;
    text-shadow: 0 0 12px #87CEFA;
    background-color: rgba(135, 206, 250, 0.25);
  }}

  /* Footer */
  .footer {{
    font-style: italic;
    font-size: 1.6rem;
    color: #ddd;
    padding-top: 40px;
    text-shadow: 0 0 8px rgba(255, 165, 0, 0.8);
  }}

  .emoji {{
    display: inline-block;
    animation: pulse 1.8s infinite;
    margin-left: 8px;
  }}

  @keyframes pulse {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.3); }}
  }}

  /* Responsive */
  @media (max-width: 600px) {{
    .title {{
      font-size: 2rem;
      white-space: normal;
    }}
    .cat-img {{
      width: 80vw !important;
      margin-bottom: 2rem;
    }}
    .links {{
      gap: 20px;
      font-size: 1.2rem;
      flex-wrap: wrap;
      margin-bottom: 2rem;
    }}
    .footer {{
      font-size: 1.4rem;
      padding-top: 30px;
    }}
  }}
</style>

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
    Thanks for dropping by — don’t forget to hit that follow! <span class="emoji">🙌</span>
  </div>
</div>
"""

# Display the page in Streamlit
st.markdown(page_html, unsafe_allow_html=True)
