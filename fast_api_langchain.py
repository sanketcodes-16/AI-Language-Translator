################# FAST API ######################
# pip install fastapi langchain-openai uvicorn python-dotenv langchain-core langchain
# TO test the application on webframework - FASTAPI
# uvicorn fast_api_langchain:app --reload

from fastapi import FastAPI
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv
import os 

load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Translation API", description="Translate text into different languages using OpenAI")

# Define the OpenAI API key (replace with your actual key)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define the prompt template
prompt = PromptTemplate.from_template("How to say {input} in {output_language}:\n")

# Create the chain
chain = prompt | llm

# Define a Pydantic model for request validation
class TranslationRequest(BaseModel):
    input: str
    output_language: str

# Create the endpoint
@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    """
    Endpoint to translate text into a specified language.
    
    Args:
        request (TranslationRequest): JSON payload with 'input' and 'output_language'.
    
    Returns:
        dict: The translation result.
    """
    result = chain.invoke(
        {
            "input": request.input,
            "output_language": request.output_language
        }
    )
    return {"translation": result}

# Optional: Add a root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Translation API"}