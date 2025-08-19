import tempfile
import streamlit as st
from main import image_background_remove
import cv2

# 🎨 Custom CSS for modern UI
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4338ca, #6d28d9);
    }
    .uploadedImage {
        border-radius: 16px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
        margin-top: 15px;
    }
    h1 {
        text-align: center;
        color: #e2e8f0;
        font-size: 2.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🚀 Title
st.markdown("<h1>🪄 AI Background Remover</h1>", unsafe_allow_html=True)
st.write("Upload your image and let AI remove the background instantly ✨")

# 📂 File Upload
uploaded_file = st.file_uploader("Upload your image here", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save file temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp_file.write(uploaded_file.read())
    temp_file_path = temp_file.name

    # Process Image
    with st.spinner("🧠 Removing background..."):
        output = image_background_remove(temp_file_path)

    # Show Results (Side-by-Side)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📸 Original Image")
        st.image(temp_file_path, use_container_width=True, caption="Uploaded Image", output_format="auto")

    with col2:
        st.subheader("✨ Background Removed")
        st.image(output, channels="BGR", use_container_width=True, caption="Result", output_format="auto")

    # ✅ Download Button
    st.download_button(
        label="⬇️ Download Processed Image",
        data=cv2.imencode(".png", output)[1].tobytes(),
        file_name="background_removed.png",
        mime="image/png"
    )
