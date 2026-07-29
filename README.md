# 🌍 AI Language Translator

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black?style=for-the-badge&logo=openai)

</p>

<p align="center">
An AI-powered multilingual translation application built using <b>FastAPI</b>, <b>LangChain</b>, <b>OpenAI</b>, and <b>Streamlit</b>.
</p>

---

# 📖 Overview

AI Language Translator is a modern web application that translates text into multiple languages using OpenAI Large Language Models.

The project consists of two parts:

- 🚀 FastAPI Backend
- 🎨 Streamlit Frontend

The backend processes translation requests using LangChain and OpenAI, while the frontend provides a clean and interactive user interface.

---

# ✨ Features

- 🌍 Translate text into multiple languages
- ⚡ FastAPI REST API
- 🤖 OpenAI + LangChain Integration
- 🎨 Attractive Streamlit UI
- 📱 Responsive Design
- 🔒 Environment Variable Support
- 📚 Interactive API Documentation
- 📝 Input Validation using Pydantic
- ⚡ Lightweight and Fast

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| LangChain | LLM Framework |
| OpenAI | Translation Model |
| Pydantic | Request Validation |
| Requests | API Communication |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```text
AI-Language-Translator/
│
├── fast_api_langchain.py
├── streamlit_app.py
├── run_app.bat
├── requirements.txt
├── .env
├── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-Language-Translator.git

cd AI-Language-Translator
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# ▶️ Running the Application

## Option 1

Run FastAPI

```bash
uvicorn fast_api_langchain:app --reload
```

Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## Option 2 (Recommended)

Simply double-click

```
run_app.bat
```

This automatically starts

- FastAPI Server
- Streamlit Application

---

# 🌐 Application URLs

| Service | URL |
|----------|-----|
| FastAPI | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| Streamlit | http://localhost:8501 |

---

# 📸 Screenshots

## Streamlit UI

> Add screenshot here

```
images/home.png
```

---

## Translation Result

> Add screenshot here

```
images/result.png
```

---

## Swagger Documentation

> Add screenshot here

```
images/swagger.png
```

---

# 📡 API Endpoint

## Translate Text

**POST**

```
/translate/
```

### Request

```json
{
    "input": "Hello, How are you?",
    "output_language": "Hindi"
}
```

### Response

```json
{
    "translation": "नमस्ते, आप कैसे हैं?"
}
```

---

# 🌎 Supported Languages

- English
- Hindi
- Marathi
- French
- German
- Spanish
- Arabic
- Chinese
- Japanese
- Russian
- Tamil
- Telugu
- Gujarati
- Kannada

---

# 🚀 Future Improvements

- 🌍 Detect Input Language Automatically
- 🔊 Text-to-Speech
- 🎤 Speech-to-Text
- 📄 PDF Translation
- 📋 Translation History
- ⭐ Favorite Translations
- 🌐 Dark/Light Theme
- 🤖 Support Multiple AI Models
- 📱 Mobile-Friendly UI

---

# 📦 Requirements

```
fastapi
uvicorn
streamlit
requests
python-dotenv
pydantic
langchain
langchain-core
langchain-openai
openai
tiktoken
```

---

# 👨‍💻 Author

**Sanket More**

AI Developer | Python Developer | Data Engineer

GitHub:
https://github.com/sanketcodes-16

LinkedIn:
(Add Your LinkedIn URL)

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

# 📄 License

This project is licensed under the MIT License.

---

<p align="center">

Made with ❤️ using Python • FastAPI • Streamlit • LangChain • OpenAI

</p>