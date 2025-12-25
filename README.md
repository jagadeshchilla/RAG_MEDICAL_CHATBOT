# Medical RAG Chatbot

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jagadeshchilla/RAG_MEDICAL_CHATBOT)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-%23000000.svg?style=for-the-badge&logo=langchain&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-vector%20store-0078D4?style=for-the-badge&logo=facebook&logoColor=white)
![Mistral AI](https://img.shields.io/badge/Mistral%20AI-LLM-FF6B6B?style=for-the-badge&logo=ai&logoColor=white)

A Retrieval-Augmented Generation (RAG) based medical chatbot application that leverages Large Language Models (LLM) to provide intelligent medical information retrieval and question-answering capabilities. The application is fully containerized and deployed using a complete CI/CD pipeline with Jenkins, Docker, AWS ECR, and AWS App Runner.

## Table of Contents

- [Overview](#overview)
- [Architecture & Workflow](#architecture--workflow)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Documentation](#documentation)

## Overview

This Medical RAG Chatbot is designed to:
- Process and chunk medical documents (PDFs)
- Generate embeddings using Hugging Face models
- Store vectors in FAISS for efficient similarity search
- Retrieve relevant context using LangChain
- Generate accurate responses using Mistral AI (via Groq)
- Provide a web interface using Flask
- Automate deployment through Jenkins CI/CD pipeline

## Architecture & Workflow

The complete development and deployment workflow is illustrated in the following diagram:

![Medical RAG Workflow](Medical+RAG+Workflow%20(1).png)

### Workflow Components

#### 1. **Project Setup and Configuration** (Teal)
- Project and API setup
- Virtual environment and logging configuration
- Custom exception handling
- Configuration management
- Environment variables access

#### 2. **Data Processing and Storage** (Orange)
- PDF document loading
- Text chunking with LangChain
- Embedding generation
- Vector storage in FAISS
- Data loader integration

#### 3. **LLM and Retrieval** (Purple)
- LLM setup (Mistral AI)
- Retriever configuration
- Application integration

#### 4. **Application Layer** (Green)
- Main application code
- Flask backend
- HTML/CSS frontend

#### 5. **Versioning and Deployment** (Blue)
- GitHub version control
- Dockerfile creation
- Jenkins CI/CD setup
- GitHub-Jenkins integration
- Docker image build and Trivy security scanning
- AWS ECR push
- AWS App Runner deployment

## Features

- **Intelligent Document Processing**: Extract and process medical documents from PDFs
- **RAG Architecture**: Retrieval-Augmented Generation for accurate, context-aware responses
- **Security Scanning**: Automated vulnerability scanning with Aqua Trivy
- **CI/CD Pipeline**: Fully automated build, test, and deployment pipeline
- **Cloud Deployment**: Deployed on AWS App Runner for scalability
- **Containerized**: Docker-based deployment for consistency
- **Vector Search**: Efficient similarity search using FAISS
- **LLM Integration**: Powered by Mistral AI via Groq API

## Tech Stack

### Core Technologies
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for backend API
- **LangChain**: Framework for LLM applications
- **FAISS**: Vector similarity search library
- **Hugging Face**: Embedding models and transformers
- **Mistral AI**: Large Language Model (via Groq API)
- **pypdf**: PDF document processing

### DevOps & Infrastructure
- **Docker**: Containerization
- **Jenkins**: CI/CD automation
- **AWS ECR**: Container registry
- **AWS App Runner**: Serverless container deployment
- **Aqua Trivy**: Security vulnerability scanning
- **GitHub**: Version control

## Prerequisites

Before you begin, ensure you have the following installed and configured:

- [ ] **Python 3.8+** installed
- [ ] **Docker Desktop** installed and running
- [ ] **Git** installed
- [ ] **GitHub account** with repository access
- [ ] **AWS account** with appropriate IAM permissions
- [ ] **API Keys**:
  - Hugging Face API token
  - Groq API key
  - AWS Access Key and Secret Key

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/jagadeshchilla/RAG_MEDICAL_CHATBOT.git
cd RAG_MEDICAL_CHATBOT
```

### 2. Create Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

For Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
HF_TOKEN="your_huggingface_token"
HUGGINGFACEHUB_API_KEY_TOKEN="your_huggingface_token"
GROQ_API_KEY="your_groq_api_key"
```

### 5. Run the Application

```bash
python app/application.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── application.py          # Main Flask application
│   ├── common/
│   │   ├── custom_exception.py # Custom exception handling
│   │   └── logger.py           # Logging configuration
│   ├── components/
│   │   ├── data_loader.py      # Data loading utilities
│   │   ├── embeddings.py       # Embedding generation
│   │   ├── llm.py              # LLM setup and configuration
│   │   ├── pdf_loader.py       # PDF document loading
│   │   ├── retriever.py        # Retrieval logic
│   │   └── vector_store.py     # FAISS vector store
│   ├── config/
│   │   └── config.py           # Configuration management
│   └── templates/
│       └── index.html          # Frontend HTML template
├── custom_jenkins/
│   └── Dockerfile              # Jenkins Docker configuration
├── data/
│   └── *.pdf                   # Medical documents
├── vectorstore/
│   └── db_faiss/               # FAISS vector database
├── logs/                       # Application logs
├── Dockerfile                  # Application Dockerfile
├── Jenkinsfile                 # CI/CD pipeline definition
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
└── .env                        # Environment variables
```

## CI/CD Pipeline

The project includes a complete CI/CD pipeline configured in the `Jenkinsfile`:

### Pipeline Stages

1. **Clone GitHub Repo**: Checkout source code from GitHub
2. **Build, Scan, and Push Docker Image to ECR**:
   - Build Docker image
   - Security scan with Trivy
   - Push to AWS ECR
3. **Deploy to AWS App Runner**: Trigger deployment to AWS App Runner

### Jenkins Setup

For detailed Jenkins setup instructions, see the [Full Documentation](#documentation) section below.

## Documentation

For comprehensive setup and deployment instructions, please refer to the [FULL_DOCUMENTATION.md](FULL_DOCUMENTATION.md) file, which includes:

### 1. Jenkins Setup for Deployment
- Creating Jenkins setup directory and Dockerfile
- Building and running Jenkins container
- Installing Python and required tools
- Accessing Jenkins dashboard

### 2. Jenkins Integration with GitHub
- Generating GitHub Personal Access Token
- Adding credentials to Jenkins
- Creating pipeline jobs
- Configuring GitHub webhooks

### 3. Build Docker Image, Scan with Trivy, and Push to AWS ECR
- Installing Trivy in Jenkins container
- Installing AWS plugins
- Creating IAM user and credentials
- Installing AWS CLI
- Creating ECR repository
- Configuring build and push stages

### 4. Deployment to AWS App Runner
- IAM user permissions setup
- AWS App Runner service configuration
- Automated deployment pipeline

## Security

- **Environment Variables**: Sensitive data stored in `.env` file (not committed to git)
- **Security Scanning**: Automated vulnerability scanning with Aqua Trivy
- **IAM Roles**: Least privilege access for AWS services
- **GitHub Tokens**: Secure token-based authentication

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Notes

- Ensure Docker Desktop is running before building Jenkins container
- The Jenkinsfile is already configured in the repository
- Make sure all environment variables are set before running the application
- The vector store will be created automatically on first run

## Success Indicators

When the pipeline completes successfully, you should see:
- GitHub repository cloned in Jenkins workspace
- Docker image built and scanned
- Image pushed to AWS ECR
- Application deployed to AWS App Runner
- Application accessible via App Runner URL

---

**Built for Medical AI Applications**

