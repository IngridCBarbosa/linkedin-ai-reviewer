# 🤖 LinkedIn AI Reviewer

An AI-powered CLI tool designed to review, improve, and optimize LinkedIn posts using Google Gemini.

This project was created to study and practice:

- AI integrations
- Prompt engineering
- CLI application development
- Software architecture for AI tools
- Modular and scalable project organization

---

## 🎯 Purpose

The main goal of this project is to build a developer-focused AI tool capable of reviewing LinkedIn content and improving it based on different communication styles.

The tool aims to help users create more:

- professional
- engaging
- concise
- recruiter-friendly
- technical

LinkedIn posts using generative AI.

---

## 🚀 Features

- Review LinkedIn posts using AI
- Improve grammar and readability
- Generate more engaging versions
- Support different writing styles
- Command-line interface (CLI)
- Externalized prompts for easier experimentation

---

## 🧱 Project Structure

```bash
linkedin-ai-reviewer/
│
├── main.py
├── config.py
├── .env
├── requirements.txt
│
├── prompts/
│   ├── improve_post.txt
│   ├── recruiter_style.txt
│   └── technical_style.txt
│
├── services/
│   └── gemini_service.py
│
├── core/
│   ├── reviewer.py
│   └── formatter.py
│
├── cli/
│   └── commands.py
│
├── tests/
│   └── test_reviewer.py
│
└── README.md