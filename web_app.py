import streamlit as st
from PIL import Image
import os, base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Luxury Image ➜ PDF Converter", page_icon="💎", layout="centered")

# ---------- LOAD BACKGROUND ----------
bg_path = "background.png.jpg"
if os.path.exists(bg_path):
    with open(bg_path, "rb") as f:
        bg_data = base64.b64encode(f.read()).decode()
else:
    bg_data = ""

# ---------- SIDEBAR CONTROLS ----------
st.sidebar.header("🎨 Visual Customization")
bg_speed = st.sidebar.slider("🌈 Background Animation Speed", 5, 30, 12)
st.sidebar.slider("✨ Particle Speed", 1, 6, 2)
st.sidebar.slider("🫧 Particle Density", 20, 200, 80)
st.sidebar.slider("💎 Glass Blur Intensity", 5, 25, 15)

# ---------- STYLING ----------
page_bg = f"""
<style>
/* ---------- MAIN BACKGROUND ---------- */
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
                url("data:image/jpg;base64,{bg_data}") no-repeat center center fixed !important;
    background-size: cover !important;
    animation: bgZoom {bg_speed}s ease-in-out infinite alternate;
}}
@keyframes bgZoom {{
    0% {{ transform: scale(1); }}
    100% {{ transform: scale(1.1); }}
}}

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {{
    background: rgba(255, 255, 255, 0.92) !important;
    border-right: 3px solid rgba(255, 215, 0, 0.8);
    box-shadow: 5px 0 20px rgba(255, 215, 0, 0.3);
    border-top-right-radius: 18px;
    border-bottom-right-radius: 18px;
}}
[data-testid="stSidebar"] * {{
    color: #1a1a1a !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}}
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: #000 !important;
    font-weight: 800 !important;
    text-shadow: 0 0 6px rgba(255, 215, 0, 0.4);
}}

/* ---------- HEADER ---------- */
[data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
h1 {{
    text-align: center;
    font-family: 'Algerian', serif;
    font-size: 46px;
    background: -webkit-linear-gradient(#FFD700, #FFEA00, #FFF59D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 25px rgba(255,215,0,0.6);
}}

/* ---------- UPLOAD SECTION ---------- */
div[data-testid="stFileUploader"] > section {{
    background: #ffffffcc !important;
    border: 2px solid rgba(255,215,0,0.6) !important;
    border-radius: 18px !important;
    box-shadow: 0 6px 18px rgba(255, 215, 0, 0.25) !important;
    padding: 15px !important;
}}
div[data-testid="stFileUploader"] p {{ color: #000 !important; font-weight: 600 !important; }}
div[data-testid="stFileUploader"] small {{ color: #444 !important; }}

/* ---------- PREMIUM “Browse Files” BUTTON ---------- */
div[data-testid="stFileUploader"] > section > div > div > div > button {{
    background: linear-gradient(135deg, #FFD700, #FFEA00, #FFF59D) !important;
    color: #2c2c2c !important;
    border: 1px solid rgba(255, 215, 0, 0.6) !important;
    border-radius: 10px !important;
    padding: 0.7rem 1.5rem !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
    transition: all 0.3s ease-in-out !important;
}}
div[data-testid="stFileUploader"] > section > div > div > div > button:hover {{
    background: linear-gradient(135deg, #FFF9C4, #FFD700, #FFC107) !important;
    transform: scale(1.05) !important;
}}

/* ---------- INPUT BOX ---------- */
input[type="text"] {{
    background: #ffffffcc !important;
    color: #000 !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,215,0,0.6) !important;
    font-size: 15px !important;
    padding: 10px !important;
    box-shadow: 0 4px 10px rgba(255,215,0,0.15);
}}

/* ---------- LABELS FIX ---------- */
label[data-testid="stMarkdownContainer"] p {{
    color: #000 !important;
    font-weight: 800 !important;
    background: #ffffffc9 !important;
    border: 1px solid rgba(255,215,0,0.6);
    padding: 6px 10px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(255,215,0,0.4);
    width: fit-content;
    margin-bottom: 8px;
}}

/* ---------- CONVERT BUTTON ---------- */
.stButton>button {{
    width: 100%;
    border: none;
    border-radius: 15px;
    background: linear-gradient(135deg, #FFD54F, #FFC107, #FFB300);
    color: #212121;
    font-weight: 800;
    font-size: 1.1rem;
    padding: 0.9rem;
    box-shadow: 0 6px 25px rgba(255,215,0,0.4);
    transition: all 0.4s ease;
}}
.stButton>button:hover {{
    transform: scale(1.06);
    background: linear-gradient(135deg, #FFEB3B, #FFD700, #FFCA28);
    box-shadow: 0 10px 35px rgba(255,215,0,0.6);
}}

/* ---------- FOOTER ---------- */
footer {{visibility: hidden;}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>💎 Image ➜ PDF Converter</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;font-size:18px;color:white;'>Turn your images into luxury-grade PDFs — with glow, shine, and gold aesthetics ✨</p>", unsafe_allow_html=True)
st.write("---")

# ---------- MAIN SECTION ----------
uploaded_files = st.file_uploader("📸 Upload Your Images", type=["jpg","jpeg","png"], accept_multiple_files=True)
pdf_name = st.text_input("📝 Enter PDF File Name", "MyLuxuryPDF.pdf")

if st.button("🚀 Convert to PDF"):
    if not uploaded_files:
        st.error("⚠️ Please upload at least one image.")
    else:
        try:
            images = [Image.open(f).convert("RGB") for f in uploaded_files]
            images[0].save(pdf_name, save_all=True, append_images=images[1:])
            st.success(f"✅ PDF Created Successfully: {pdf_name}")
            with open(pdf_name, "rb") as f:
                st.download_button("📥 Download Your PDF", f, file_name=pdf_name, mime="application/pdf")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# ---------- FOOTER ----------
st.markdown("""
    <hr><center style='color:#FFD700;font-size:15px;'>
    © 2025 | Designed by <b>You</b> 💛 | Powered by Lunar Orbit
    </center>
""", unsafe_allow_html=True)



# python -m streamlit run web_app.py