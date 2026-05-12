import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Matcher", page_icon="📄")

st.title("📄 Strict AI Resume Analyzer")
st.markdown("---")

jd_text = st.text_area("📋 Paste Job Description (JD)", height=200)
uploaded_file = st.file_uploader("📂 Upload Candidate Resume (PDF)", type="pdf")

if st.button("🚀 Calculate Strict Score"):
    if not jd_text or not uploaded_file:
        st.warning("Please provide both JD and Resume.")
    else:
        with st.spinner("Analyzing with Strict Rules..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                data = {"jd_text": jd_text}
                
                response = requests.post("http://localhost:8001/analyze", data=data, files=files)
                
                if response.status_code == 200:
                    result = response.json()["analysis"]
                    
                    # Highlight Logic
                    if "REJECTED" in result.upper():
                        st.error("🚨 VERDICT: REJECTED")
                    else:
                        st.success("✅ VERDICT: SHORTLISTED")
                    
                    st.markdown("### 📊 Detailed Report")
                    st.info(result)
                else:
                    st.error("Backend Error!")
            except Exception as e:
                st.error(f"Connection Failed: {e}")

st.markdown("---")
st.caption("Powered by RAG Pipeline | Python 3.14 Compatible")
