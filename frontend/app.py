import streamlit as st
import requests

st.title("📄 Document Intelligence Platform")
st.write("Pure Python Frontend + FastAPI + MinIO S3 + K8s")

uploaded_file = st.file_uploader("Choose a document", type=["pdf", "png", "jpg", "txt"])

if uploaded_file is not None:
    if st.button("Process & Upload to S3"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        # Backend Service Endpoint (Kubernetes Service Name)
        backend_url = "http://backend-service:8000/upload/"
        
        try:
            response = requests.post(backend_url, files=files)
            if response.status_code == 200:
                st.success(f"Success: {response.json()}")
            else:
                st.error("Upload failed")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")