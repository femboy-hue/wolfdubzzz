import streamlit as st

# --- FULL PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="Dubzzz_Valo Hub", page_icon="✨")

# --- BACKGROUND IMAGE (FULL WIDTH) ---
st.image("starry_sky.png", use_column_width=True)

# --- CENTERED PROFILE PICTURE ---
st.markdown(
    """
    <div style='text-align: center; margin-top: -60px;'>
        <img src='cat_pfp.png' width='180' style='border-radius: 50%; border: 4px solid #fff;'/>
    </div>
    """,
    unsafe_allow_html=True
)

# --- MAIN TITLE AND DESCRIPTION ---
st.markdown(
    """
    <div style='text-align: center; color: white;'>
        <h1 style='font-size: 42px;'>✨ Dubzzz_Valo's Streaming Hub ✨</h1>
        <p style='font-size: 18px; margin-top: -10px;'>Welcome to the official hub — connect with me below 💫</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SOCIAL LINKS WITH EMOJIS ---
st.markdown(
    """
    <div style='text-align: center; font-size: 20px; margin-top: 20px;'>
        <p>
            🔴 <a href="https://www.youtube.com/@Dubzzz_Valo" style="text-decoration: none; color: #FF0000;"><b>YouTube</b></a> |
            📸 <a href="https://www.instagram.com/dubzzz_valo/" style="text-decoration: none; color: #C13584;"><b>Instagram</b></a> |
            🎧 <a href="https://www.tiktok.com/@dubzzz_valo" style="text-decoration: none; color: #000;"><b>TikTok</b></a> |
            🎮 <a href="https://www.twitch.tv/dubzzz_valo" style="text-decoration: none; color: #6441A5;"><b>Twitch</b></a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SPACING ---
st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- THANK YOU FOOTER W/ SIDE DECORATION ---
st.markdown(
    """
    <div style='display: flex; justify-content: space-between; align-items: center; background-c
