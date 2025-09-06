.stApp {
    background-image: url("data:image/png;base64,{background_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.85);
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;

    /* Background starfield animation */
    animation: starfieldMove 120s linear infinite;
}

.cat-img {
    width: 300px !important;
    border-radius: 20px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6);
    margin-bottom: 2rem;
    transition: transform 0.3s ease;
    display: block;
    margin-left: auto;
    margin-right: auto;
    position: relative;
    z-index: 2;
    /* NO animation here so it stays still */
}

.cat-img:hover {
    transform: scale(1.05);
}

/* Floating emojis container */
.floating-icons {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
    overflow: visible;
}

/* Individual floating emoji styles with different animations and delays */
.floating-icons span {
    position: absolute;
    font-size: 1.5rem;
    opacity: 0.8;
    user-select: none;
    filter: drop-shadow(0 0 2px #00ffff);
    animation-timing-function: ease-in-out;
}

.star {
    color: #fffacd;
    animation: floatUp 10s linear infinite;
}

.heart {
    color: #ff4081;
    animation: floatSide 8s ease-in-out infinite;
}

.play {
    color: #00ffea;
    animation: floatUp 12s linear infinite;
}

.bolt {
    color: #ffff00;
    animation: floatSide 7s ease-in-out infinite;
}
