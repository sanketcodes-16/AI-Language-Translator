@echo off
title AI Translator App

echo ==========================================
echo      Starting FastAPI Server...
echo ==========================================

start cmd /k "uvicorn fast_api_langchain:app --reload"

timeout /t 5 > nul

echo ==========================================
echo      Starting Streamlit App...
echo ==========================================

start cmd /k "streamlit run streamlit_app.py"

echo.
echo ==========================================
echo  FastAPI  : http://127.0.0.1:8000
echo  Swagger  : http://127.0.0.1:8000/docs
echo  Streamlit: http://localhost:8501
echo ==========================================

pause