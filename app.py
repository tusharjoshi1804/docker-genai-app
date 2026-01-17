from fastapi import FastAPI, Query
from transformers import pipeline
import wikipedia

# ---------------- APP CONFIG ----------------
app = FastAPI(
    title="Text2Text Generative AI API",
    description="Text generation using Hugging Face + Wikipedia context",
    version="1.2"
)

# ---------------- MODEL LOADING ----------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

# ---------------- HOME ROUTE ----------------
@app.get("/")
def home():
    return {
        "message": "Text2Text Generative AI API is running",
        "docs": "/docs"
    }

# ---------------- GENERATE ROUTE ----------------
@app.get("/generate")
def generate(
    text: str = Query(
        ...,
        min_length=3,
        description="Text prompt for generation"
    )
):

    # -------- Fetch Wikipedia Context --------
    try:
        wiki_summary = wikipedia.summary(
            text,
            sentences=1,
            auto_suggest=False
        )
        wiki_summary = wiki_summary.replace("\n", " ").strip()
        wiki_summary = wiki_summary[:400]
    except Exception:
        wiki_summary = ""

    # -------- Prompt Engineering --------
    prompt = f"""
You are a helpful AI assistant.
Answer clearly and accurately in simple language.
Ignore unrelated information.
Question:
{text}
Helpful reference (if relevant):
{wiki_summary}
Answer:
"""

    # -------- Text Generation --------
    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    return {
        "input": text,
        "output": result[0]["generated_text"]
    }
