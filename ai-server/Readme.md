# Getting Started with the AI Server Project

This guide will help you set up the AI Server project on your local machine for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository to your local machine.

2. Navigate to the `ai-server` directory where the `requirements.txt` file is located.

3. Install the required Python packages by running the following command in your terminal:
   pipenv shell
   pip install -r requirements.txt
   uvicorn app:app --reload
