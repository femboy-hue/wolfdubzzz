import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Hub", layout="wide")

st.title("✨ Dubzzz_Valo's Streaming Hub ✨")

st.write("Welcome to Dubzzz_Valo's official streaming hub! Connect with me on my social platforms:")

st.markdown("""
- 🎥 [YouTube](https://www.youtube.com/@Dubzzz_Valo)
- 📸 [Instagram](https://www.instagram.com/dubzzz_valo/)
- 🎵 [TikTok](https://www.tiktok.com/@dubzzz_valo)
- 🎮 [Twitch](https://www.twitch.tv/dubzzz_valo)
""")

# Display profile pic + background side by side
col1, col2 = st.columns(2)

with col1:
    st.image("profile_pic.png", caption="Dubzzz_Valo", width=250)

with col2:
    st.image("starry_sky.png", caption="Starry Night Vibes 🌌", width=400)
