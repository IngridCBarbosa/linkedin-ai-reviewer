# LinkedIn AI Reviewer

An AI-powered application designed to help users improve and refine their LinkedIn posts before publishing.

This project was created as a hands-on learning experience to explore software architecture, API development, authentication, and AI integrations while building a real-world application.

## Goals

The main goals of this project are:

* Learn and apply different software architecture patterns.
* Build a scalable backend using FastAPI.
* Integrate Large Language Models (LLMs) such as Gemini.
* Implement authentication using Firebase.
* Evolve the application from a CLI tool into a full web application.
* Practice clean architecture principles and separation of concerns.

## Current Architecture

```text
FastAPI
    ↓
Reviewer Layer
    ↓
AI Provider
    ↓
Gemini
```

## Features

### Implemented

* FastAPI application setup
* Health check endpoint
* Prompt-based LinkedIn post review workflow
* Gemini AI integration
* Environment variable management
* Error handling
* Separation between API, business logic, and AI integration layers

### In Progress

* Firebase Authentication
* Protected API endpoints
* AI Provider abstraction layer
* Frontend UI

### Planned

* User authentication with Firebase
* Review history
* Multiple writing styles
* Hashtag generation
* Engagement scoring
* Copy-to-clipboard support
* Docker support
* CI/CD pipeline
* Deployment to cloud platforms

## Project Structure

```text
linkedin-ai-reviewer/
│
├── api/
│   ├── dependencies/
│   ├── routes/
│   └── schemas/
│
├── core/
│   └── reviewer.py
│
├── services/
│   ├── gemini_service.py
│   └── firebase_service.py
│
├── prompts/
│
├── main.py
├── requirements.txt
└── .env
```

## Tech Stack

* Python
* FastAPI
* Firebase Authentication
* Google Gemini
* Uvicorn

## Running Locally

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

### Run the API

```bash
uvicorn main:app --reload
```

### API Documentation

FastAPI automatically generates interactive documentation:

```text
http://localhost:8000/docs
```

## Learning Journey

This repository is intentionally being built incrementally.

Each feature is implemented through small tasks to better understand:

* API design
* Authentication and authorization
* Software architecture
* AI integrations
* Scalability and maintainability
* Backend engineering best practices
