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
Returns a simple status message confirming that the API is active.

### Text Generation
Generates a simple explanation for the given input text.

GET /generate?text=your_query_here
**Query Parameter**

- `text` (string, required): Input prompt for generation.

**Example Request**
/generate?text=Explain Docker in simple words
**Example Response**

```json
{
  "input": "Explain Docker in simple words",
  "output": "Docker is a tool that packages applications into containers so they run the same on any system."
}

## Swagger Documentation

FastAPI automatically generates interactive API documentation.

/docs
Using this interface we can test endpoints directly from the browser.

## Cloud Deployment

This application is containerized using Docker and deployed on **Hugging Face Spaces**.  
The platform automatically builds the Docker image, manages the runtime environment, and exposes the API publicly.

Key deployment characteristics:

- Docker-based container is build  
- Automatic image build and startup on cloud infrastructure  
- Public HTTPS endpoint  
- Auto-restart on failure  


## Live Application

Live API:  
https://tusharj18-docker-genai-api.hf.space  

Swagger UI:  
https://tusharj18-docker-genai-api.hf.space/docs