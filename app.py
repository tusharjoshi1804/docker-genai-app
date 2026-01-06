from fastapi import FastAPI, Query
from transformers import pipeline
import wikipedia

app = FastAPI(
    title="Text2Text Generative AI API",
    description="Text generation using Hugging Face + Wikipedia context",
    version="1.0"
)

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

@app.get("/")
def home():
    return {
        "message": "Text2Text Generative AI API is running",
        "docs": "/docs"
    }

@app.get("/generate")
def generate(
    text: str = Query(
        ...,
        min_length=3,
        description="Text prompt for generation"
    )
):
  
    try:
        wiki_summary = wikipedia.summary(text, sentences=2)
        context = f"Use the following information to answer clearly:\n{wiki_summary}"
    except Exception:
    
        context = text

    prompt = f"""
Question: {text}
Context: {context}
Answer in simple words.
"""

    result = generator(
        prompt,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    return {
        "input": text,
        "output": result[0]["generated_text"]
    }