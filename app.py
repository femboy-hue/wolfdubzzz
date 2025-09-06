import streamlit as st

st.set_page_config(page_title="Dubzzz_Valo's Streaming Hub", layout="wide")

# CSS styles
css = """
<style>
/* Background */
.main {
    background-color: #121212;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    padding: 30px 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Title styling */
.title {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
    text-align: center;
    user-select: none;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: #bbb;
    margin-top: 5px;
    margin-bottom: 40px;
    text-align: center;
    user-select: none;
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
    margin-bottom: 50px;
}

/* Stylish links container */
.links {
    display: flex;
    justify-content: center;
    gap: 60px;
    margin-bottom: 60px;
    flex-wrap: wrap;
}
