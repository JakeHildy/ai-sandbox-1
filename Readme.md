# AI Coding Experiments

Welcome to our project, a hub for all AI coding experiments. This repository is designed to explore the capabilities of AI in coding, offering a variety of applications each tailored to demonstrate a unique aspect of AI's potential in programming and software development. Below, you'll find a brief overview of each app contained within this project.

## Applications Overview

### 1. TChat

**Location:** `lang-chain/tchat/main.py`

TChat is an AI-powered chat application that leverages the OpenAI's GPT models to simulate human-like conversations. It uses a combination of `ChatOpenAI` for generating responses and `LLMChain` to process the chat flow, making it possible to have interactive dialogues with the AI. The application dynamically generates responses based on user input, showcasing the potential of AI in creating conversational agents.

### 2. PyCode

**Location:** `lang-chain/pycode/main.py`

PyCode is an experiment in automated code generation. It uses OpenAI's models to generate Python code snippets and corresponding tests based on user-defined tasks and languages. By inputting a task and specifying a language, PyCode demonstrates AI's ability to understand programming tasks and generate syntactically correct and logically sound code, along with tests to verify the code's functionality.

### 3. Starlette Web App

**Location:** `lang-chain/starlette/app.py`

This application is a simple web server built with Starlette, showcasing how AI can be integrated into web development. It features basic routes and responses, serving as a foundation for more complex AI-driven web applications. The app demonstrates the ease with which AI functionalities can be incorporated into web services, paving the way for intelligent web ecosystems.

## Environment Configuration

Each application within this project relies on an `.env` file for configuration, specifically for storing the OpenAI API key. This key is essential for interacting with OpenAI's services and enabling the AI functionalities within each app.
