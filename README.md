# Text2Text GenAI API 

A Dockerized **Text-to-Text Generative AI API** built using **FastAPI**, **Hugging Face Transformers**, and **Wikipedia lookup**, deployed on **Hugging Face Spaces**.

This project takes a user query, optionally fetches relevant Wikipedia context, and generates a simple, human-friendly explanation using an LLM.


## 🔥 Features

- ⚡ FastAPI backend with Swagger UI
- 🤖 Hugging Face Transformer (Flan-T5)
- 📚 Wikipedia context augmentation
- 🐳 Fully Dockerized application
- ☁️ Deployed on Hugging Face Spaces
- 🧪 Interactive API testing via `/docs`


## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Model:** `google/flan-t5-base`
- **NLP:** Hugging Face Transformers
- **Context Source:** Wikipedia
- **Containerization:** Docker
- **Deployment:** Hugging Face Spaces
- **Language:** Python 3.10+

### API Endpoints

-**Health Check**

Purpose: Used to verify that the application is running and ready to accept requests.

Endpoint: GET /

-**Text Generation**

Purpose: Generates a simple explanation for the given input text.

Endpoint: GET /generate

-**Swagger Documentation**

FastAPI automatically generates interative API documentation.

Swagger UI path: /docs

-**Docker Setup (Local execution)**

This application is fully containerized using Docker and could be run locally after building the image. Once the container is running, the swagger UI is available on **port 7860**.

## Live Deployment 

This app is deployed on Hugging face spaces using Docker.

[Live API](https://tusharj18-text2textwithdocker.hf.space)
 
[Swagger UI](https://tusharj18-text2textwithdocker.hf.space/docs)

