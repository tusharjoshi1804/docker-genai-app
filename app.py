from fastapi import FastAPI
from transformers import pipeline

app=FastAPI()

# Load model once at startup
pipe=pipeline("text2text-generation",model="google/flan-t5-small")

@app.get("/")
def home():
    return{"message":"Hello World"}

@app.get("/generate")
def generate(text:str):
    result=pipe(text)
    return{"output":result[0]["generated_text"]}
