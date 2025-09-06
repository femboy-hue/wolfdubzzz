import streamlit as st

# Set page layout
st.set_page_config(layout="wide")

# Paths to your uploaded images
star_bg_path = "/mnt/data/starry_sky.png"
cat_img_path = "/mnt/data/cat.png"

# CSS for layout and styling
st.markdown(f"""
<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #0b0c10;
    color: #fff;
    overflow-x: hidden;
}}
.main {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 0 5vw;
}}
.container {{
    display: flex;
    width: 100%;
    max-width: 1200px;
}}
.left {{
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.title {{
    font-size: 3rem;
    font-weight: 900;
    color: #ff4d4d;
    text-align: center;
    margin-bottom: 40px;
}}
.links {{
    display: flex;
    flex-direction: column;
    gap: 25px;
    align-items: flex-start;
}}
a {{
    color: #4da6ff;
    font-weight: bold;
    font-size: 1.25rem;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: color 0.3s, transform 0.3s;
}}
a:hover {{
    color: #ff6666;
    transform: scale(1.05);
    cursor: pointer;
}}
.footer {{
    font-style: italic;
    font-size: 1rem;
    color: #bbb;
    text-align: center;
    margin-top: 40px;
}}
.right {{
    flex: 1;
    position: relative;
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
    overflow: hidden;
}}
.star-bg {{
    position: absolute;
    top: 0;
    right: 0;
    width: 60vw;
    height: 100vh;
    background: url("file://{star_bg_path}") no-repeat center center;
    background-size: cover;
    z-index: 0;
    filter: brightness(0.8);
    border-radius: 0 0 0 40px;
}}
.cat {{
    position: relative;
    width: 250px;
    height: auto;
    margin-top: 40px;
    z-index: 1;
    filter: drop-shadow(0 0 10px rgba(255, 102, 102, 0.7));
}}
@media (max-width: 768px) {{
    .container {{
        flex-direction: column;
        align-items: center;
    }}
    .right {{
        width: 100%;
        justify-content: center;
        margin-top: 20px;
    }}
    .star-bg {{
        width: 100vw;
        height: 300px;
        border-radius: 40px 40px 0 0;
    }}
    .cat {{
        width: 150px;
        margin-top: 10px;
    }}
    .title {{
        font-size: 2.25rem;
    }}
}}
</style>
""", unsafe_allow_html=True)

# Main HTML content with images inserted
st.markdown(f"""
<div class="main">
  <div class=
