# **🚀 RAG Project — Retrieval-Augmented AI Assistant**

A lightweight, intelligent Retrieval-Augmented Generation (RAG) chatbot that answers questions using your own documents, combined with the reasoning power of Large Language Models.

**👉 Live Demo:** https://rag-project-assistant.streamlit.app/  
**👉 GitHub Repo:** https://github.com/kuldeep681/Rag_Project1

---

## 📌 **What is RAG Project?**

Modern AI models generate great answers, but they hallucinate when they don't know something.RAG Project fixes this by combining an LLM with a vector database, enabling the assistant to:

- Read your documents

- Understand them using embeddings

- Retrieve relevant pieces when you ask a question

- Use an LLM to generate accurate, grounded answers

This project is my first complete step into building a production-style RAG application.

---

## 🌟 **Key Features**

### 🔍 **Document Understanding**

- Upload text/PDF/notes into the data/ folder

- System embeds & stores them using a vector store

- Retrieval pulls only the context needed for your query

### 🤖 **AI-Powered Reasoning**

- LLM uses retrieved chunks to answer with context

- Reduces hallucination dramatically

- Ensures answers are grounded in your data

### 💬 **Chat Interface**

- Use CLI or GUI (gui.py)

- Ask natural language questions

- Get instant answers from your knowledge base

### ⚙ **Modular Architecture**

- **assistant.py —** Core logic (RAG pipeline)

- **prompts.py —** Custom system prompts

- **gui.py —** User interface

- **app.py —** Optional wrapper

- **data/ —** Your knowledge source

### 🧩 **Easy to Customize**

You can swap:

- Embedding models

- LLM backend

- Vector database

- Prompt style

- User interface

---

## 🏗 **Project Architecture**

```bash
Rag_Project1/
│
├── data/                   # Knowledge base documents
│     ├── employees.py
│     └── docs.pdf          # Portfolio documents
│
├── assistant.py            # Core RAG logic (embed → retrieve → generate)
├── prompts.py              # Prompt templates for the LLM
├── gui.py                  # Simple graphical chat interface
├── app.py                  # app runner (CLI or integration)
├── .gitignore
├── requirements.txt        # Python dependencies
└── README.md               # This documentation
```

---

## ⚡ **How RAG Works**

1️⃣ **Documents Loaded**
Files in /data are read and preprocessed.

2️⃣ **Embeddings Generated**
Each document chunk is converted into a vector representation.

3️⃣ **Stored in Vector DB**
Vectors stored for fast semantic search.

4️⃣ **User Asks a Question**
Query is turned into an embedding.

5️⃣ **Retriever Finds Relevant Chunks**
Top matching passages are extracted.

6️⃣ **LLM Generates Final Answer**
Assistant combines retrieved info with reasoning.

---

## 💻 **Local Setup (Step-by-Step)**

1. **Clone Repository**

```bash
git clone https://github.com/kuldeep681/Rag_Project1.git
cd Rag_Project1
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Add Your Documents**

Place any .txt, .md, .pdf, or notes inside:

```bash
data/
```

4. **Add Your API Key**

If using OpenAI / Groq / Gemini / Ollama:

Create a .env file:

```bash
OPENAI_API_KEY=your_key_here
```

5. **Run the Assistant**

CLI Mode:

```bash
python assistant.py
```

**You can now ask anything like:**

```bash
"What is your hobby?"
"Summarize the experience part."
"Give a short explanation of X from my data."
```

---

## 🚀 **Deployment Guide**

### 🔧 **Local Deployment**

No external server needed.
All processing runs locally using your machine.

### 🌐 **Cloud Deployment**

The entire application (UI + backend logic + embeddings + retrieval + LLM inference) is deployed on Streamlit Cloud.
No separate backend server is required — Streamlit handles both the interface and the processing pipeline within a single unified environment.But put environment variables in secret key in streamlit.

---

## 📌 **Use Cases**

- Personal knowledge assistant

- College notes summarizer

- FAQ/support bot

- Custom chatbot for companies

- Domain-specific learning assistant

- Glossary generator

---

## 🧠 **Skills Demonstrated**

- Python Programming

- Retrieval-Augmented Generation (RAG)

- Vector Embeddings (Sentence Transformers / OpenAI Embeddings)

- Prompt Engineering

- LLM Integration (OpenAI / Groq / Gemini)

- Basic GUI development

- Modular project structuring

- Knowledge-based AI

---

## 📬 **Contact**

If you'd like help improving this RAG project or expanding it to a full intelligent assistant:

## 📧 **Email:** kuldeepmandal175514@gmail.com

## 🔗 **LinkedIn:** https://www.linkedin.com/in/kuldeep-mandal175514/

---
