# Offline AI Assistant

A local AI-powered document management application built with Django and Qwen3.5-9B.

Upload documents, extract their text, and generate Korean summaries using a locally running LLM through LM Studio.

The project focuses on integrating local AI models into a practical web application without relying on external cloud AI APIs.

## Features

- **Document Upload** – Upload PDF and TXT documents.
- **Text Extraction** – Extract and store document text.
- **Local LLM Integration** – Connect Django to LM Studio using an OpenAI-compatible API.
- **AI Summarization** – Generate Korean summaries using Qwen3.5-9B.
- **Summary Storage** – Save generated summaries in SQLite.
- **Document Management** – View uploaded documents and download original files.
- **Privacy-focused** – Run AI inference locally without sending document contents to an external AI service.

## Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| AI Model | Qwen3.5-9B |
| LLM Runtime | LM Studio |
| API | OpenAI-compatible Chat Completions API |
| HTTP Client | Python urllib |
| Environment | Python Virtual Environment |

## Architecture

```text
                User
                 |
                 v
          Django Web App
                 |
          Document Upload
                 |
                 v
          Text Extraction
                 |
                 v
             SQLite
                 |
          Summarization
                 |
                 v
          Django LLM Client
                 |
                 v
          LM Studio API
                 |
                 v
           Qwen3.5-9B
                 |
          Generated Summary
                 |
                 v
             SQLite
                 |
                 v
          Display Results
```

## Project Structure

```text
offline-ai-assistant/
│
├── config/
│   └── settings.py
│
├── documents/
│   ├── migrations/
│   ├── templates/
│   │   └── documents/
│   │       └── upload.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   └── llm.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/offline-ai-assistant.git
cd offline-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure LM Studio

1. Install and launch LM Studio.
2. Download the `qwen/qwen3.5-9b` model.
3. Load the model.
4. Start the local API server.

Default API endpoint:

```text
http://127.0.0.1:1234/v1
```

Make sure the model identifier in `documents/llm.py` matches the model loaded in LM Studio.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Start Django

```bash
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000/documents/

## How to Use

1. Open the document upload page.
2. Enter a document title.
3. Upload a supported document.
4. Django extracts and stores its text.
5. Click the **Summarize** button.
6. The extracted text is sent to the local Qwen model.
7. The generated Korean summary is saved in SQLite.
8. View the summary on the document page.

## Current Limitations

- Initial summarization limit: 20,000 characters.
- Long-document chunking is not implemented yet.
- Summarization requires LM Studio to be running.
- The current interface is a basic HTML implementation.
- Document-specific AI question answering is not implemented yet.

## Future Improvements

- [ ] Improve long-document summarization with text chunking.
- [ ] Add Markdown rendering for AI summaries.
- [ ] Implement document-specific AI question answering.
- [ ] Introduce RAG (Retrieval-Augmented Generation).
- [ ] Add semantic document search using embeddings.
- [ ] Improve the user interface and document management.

## Project Goals

This project explores how locally hosted language models can be integrated into web applications.

Through this project, I aim to develop practical experience with:

- Django backend development
- Document processing and text extraction
- Local LLM integration
- API communication
- Database management
- AI-powered application development

---

**Status:** Initial implementation / MVP

**Developer:** Minjae