import streamlit as st
import requests

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="🌍 AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>

.main {
    background: linear-gradient(to right,#141E30,#243B55);
}

.title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#00E5FF;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:white;
    margin-bottom:30px;
}

div[data-testid="stTextArea"] textarea{
    background-color:#1e293b;
    color:white;
    border-radius:10px;
}

div[data-testid="stSelectbox"]{
    background-color:#1e293b;
    border-radius:10px;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:20px;
    font-weight:bold;
    border-radius:10px;
    background:linear-gradient(to right,#00c6ff,#0072ff);
    color:white;
}

.result{
    background:#0f172a;
    padding:20px;
    border-radius:10px;
    color:#00FFAA;
    font-size:22px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------

st.markdown("<div class='title'>🌍 AI Language Translator</div>",
            unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Translate any language using OpenAI + LangChain + FastAPI</div>",
    unsafe_allow_html=True,
)

# ---------------------- LAYOUT ----------------------

col1, col2 = st.columns(2)

languages = [
    "Hindi",
    "Marathi",
    "English",
    "French",
    "German",
    "Spanish",
    "Japanese",
    "Chinese",
    "Russian",
    "Arabic",
    "Tamil",
    "Telugu",
    "Gujarati",
    "Kannada"
]

with col1:

    st.subheader("📝 Enter Text")

    text = st.text_area(
        "",
        height=220,
        placeholder="Type your text here..."
    )

with col2:

    st.subheader("🌐 Select Language")

    language = st.selectbox(
        "",
        languages
    )

    st.write("")
    st.write("")
    translate = st.button("🚀 Translate")

# ---------------------- API ----------------------

API_URL = "http://127.0.0.1:8000/translate/"

if translate:

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        payload = {
            "input": text,
            "output_language": language
        }

        try:

            with st.spinner("Translating..."):

                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:

                    result = response.json()["translation"]

                    st.markdown("## ✅ Translation")

                    st.markdown(
                        f"<div class='result'>{result}</div>",
                        unsafe_allow_html=True
                    )

                    st.success("Translation Completed Successfully.")

                else:
                    st.error(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown(
    "<div class='footer'>Made with ❤️ using Streamlit + FastAPI + LangChain + OpenAI</div>",
    unsafe_allow_html=True,
)