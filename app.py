import streamlit as st
from utils import extract_numbers

st.title("📸 Photo Bill Calculator")

uploaded_file = st.file_uploader(
    "Upload Bill Image",
    type=["jpg","jpeg","png","bmp","webp","tiff"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    numbers, total, text = extract_numbers(uploaded_file)

    st.subheader("Detected Text")
    st.write(text)

    st.subheader("Numbers Found")
    st.write(numbers)

    st.success(f"Total Amount = {total}")