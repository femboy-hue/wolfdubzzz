import streamlit as st

# Set page config
st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="wide", page_icon="🐱")

# Page background color and font style using markdown with CSS
st.markdown(
    """
    <style>
    /* Background */
    .main {
        background-color: #121212;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Title styling */
    .title {
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    /* Subtitle */
    .subtitle {
        font-size: 20px;
        color: #bbb;
        margin-top: 0;
        margin-bottom: 30px;
    }
    /* Center the profile pic */
    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 180px;
        height: 180px;
        border-radius: 90px;
        border: 3px solid #ee0979;
        box-shadow: 0 0 15px 3px #ff6a00;
        margin-bottom: 40px;
    }
    /* Stylish links container */
    .links {
        d
