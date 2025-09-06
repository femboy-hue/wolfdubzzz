import streamlit as st

# Set page config
st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", page_icon="🐾", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
/* Full screen starry night background */
body, .main {
    margin: 0; padding: 0;
    height: 100vh;
    background: url('https://i.imgur.com/c1da0445-2828-4479-abf4-b17485e1707c.png') no-repeat center center fixed;
    background-size: cover;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #fff;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
}

/* Container for top content */
.top-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30px 60px 0 60px;
}

/* Profile pic top right */
.profile-pic {
    width: 160px;
    height: 160px;
    border-radius: 80px;
    border: 3px solid #ff6a00;
    box-shadow: 0 0 20px 10px rgba(255, 106, 0, 0.8);
    object-fit: cover;
}

/* Title styling */
.title {
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    user-select: none;
    max-width: 60vw;
    text-align: left;
    padding-right: 40px;
}

/* Links container centered */
.links-container {
    display: flex;
    justify-content: center;
    margin: 40px 0 60px 0;
    gap: 45px;
}

/* Link styling */
.link {
    font-size: 20px;
    font-weight: 700;
    color: #ff6a00;
    text-decoration: none;
    transition: transform 0.3s
