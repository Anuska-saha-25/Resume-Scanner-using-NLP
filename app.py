import streamlit as st
from resume_parser import extract_resume_data
import tempfile
import os

st.set_page_config(page_title="Resume Scanner", layout="centered")

st.title("📄 Resume Scanner using NLP")
st.markdown("Upload a resume PDF to extract candidate information.")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    try:
        result = extract_resume_data(temp_path)

        st.success("✅ Resume parsed successfully!")
        st.json(result)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

    os.remove(temp_path)
