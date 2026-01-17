# Text2Text GenAI API

A Dockerized Text-to-Text Generative AI API built using FastAPI, Hugging Face Transformers, and Wikipedia context retrieval, deployed on Hugging Face Spaces.

This project accepts a user query, optionally fetches relevant Wikipedia context, and generates a clear, human-friendly explanation using a Large Language Model (LLM).


## Features

- FastAPI backend with interactive Swagger UI
- Hugging Face Transformer model (Flan-T5 Large)
- Wikipedia context augmentation for better responses
- Fully Dockerized application
- Deployed on Hugging Face Spaces
- Live API testing via `/docs`


## Tech Stack

- Backend: FastAPI  
- Model: google/flan-t5-large  
- NLP: Hugging Face Transformers  
- Context Source: Wikipedia  
- Containerization: Docker  
- Deployment: Hugging Face Spaces  
- Language: Python 3.10+


## API Endpoints

### Health Check
Used to verify that the application is running.
GET /
Copy code

Returns a simple status message.


### Text Generation
Generates a simple explanation for the given input text.
GET /generate?text=your_query_here
Copy code

Example:
/generate?text=Explain Docker in simple words
Copy code


### Swagger Documentation
FastAPI automatically generates interactive API documentation.
/docs
Copy code

Use this interface to test the API directly from the browser.


## Docker Setup (Local Execution)

This application is fully containerized using Docker and can be run locally.

### Build Image
```bash
docker build -t text2text-genai .
Run Container
Copy code
Bash
docker run -p 7860:7860 text2text-genai
Open in browser:
Copy code

http://localhost:7860/docs

### Live Deployment
This application is deployed on Hugging Face Spaces using Docker.
Live API:
https://tusharj18-docker-genai-api.hf.space
Swagger UI:
https://tusharj18-docker-genai-api.hf.space/docs

