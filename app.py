import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", page_icon="🐾")

# CSS styles
st.markdown("""
<style>
/* Full-screen starry sky background */
body, .main {
    margin: 0; padding: 0;
    height: 100vh;
    background: url('https://i.imgur.com/d06d0e8c-1389-491f-82cb-adfcdb3ff456.png') no-repeat center center fixed;
    background-size: cover;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}

/* Profile pic */
.profile-pic {
    width: 180px;
    height: 180px;
    border-radius: 90px;
    border: 3px solid #ee0979;
    box-shadow: 0 0 15px 6px rgba(255, 106, 0, 0.6); /* softer orange glow */
    margin-top: 40px;
    object-fit: cover;
}

/* Title */
.title {
    font-size: 48px;
    font-weight: 900;
    margin-top: 25px;
    margin-bottom: 25px;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    user-select: none;
}

/* Links container */
.links {
    background: rgba(0, 0, 0, 0.35);
    padding: 25px 40px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(255, 106, 0, 0.3);
    display: flex;
    flex-direction: column;
    gap: 18px; /* uniform vertical spacing */
    max-width: 280px;
    wi
