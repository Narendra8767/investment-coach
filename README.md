# Investment Coach & Market Commentary Assistant  
### (RAG-Based Conversational AI System)

##  Project Overview

The **Investment Coach & Market Commentary Assistant** is a **Retrieval-Augmented Generation (RAG)** based conversational AI chatbot designed to provide **educational investment guidance** and **neutral market commentary**.

This system is built to help users understand investment concepts and market movements **without giving financial advice or recommendations**.

The assistant combines:
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- User-uploaded PDFs
- Live market and business news
- Session-based chat memory
- ChatGPT-style UI with resume chat functionality

##  Disclaimer

> **This chatbot is strictly for educational purposes only.**  
> It does **not** provide financial advice, stock recommendations, buy/sell signals, or guarantees of returns.

##  Key Features

### 1️ Investment Coach Mode
- Explains core investment concepts such as:
  - SIP
  - Mutual Funds
  - Risk
  - Diversification
- Uses **simple language and real-world analogies**
- Avoids any form of buy/sell recommendations
- Supports **PDF-based RAG grounding** when documents are uploaded

### 2️ Market Commentary Mode
- Provides **neutral explanations** of market movements
- Uses **live business and market news**
- No predictions or investment advice
- Focuses on **macroeconomic reasoning and context**

### 3️ RAG-Based PDF Question Answering
- Users can upload PDFs directly during chat
- PDFs are:
  - Parsed
  - Chunked
  - Embedded
  - Stored in a vector database (FAISS)
- Relevant chunks are retrieved for each user query
- LLM responses are **fully grounded in uploaded documents**

### 4️ Upload PDF During Chat
- Upload PDFs at any point in a conversation using the ➕ button
- Multiple PDFs supported per session
- Each chat session maintains its **own document context**
- Enables questions like:
  - *“Summarize the PDF I uploaded”*
  - *“Explain the risk factors mentioned in the document”*

### 5️ Resume Chat (Session Persistence)
- Each chat has a unique `session_id`
- Previous chats appear in a **left sidebar**
- Users can:
  - Resume old chats
  - Start new chats
- Chat history is restored automatically on reload

### 6️ UI & Styling
- Modern **dark theme**
- ChatGPT-style message bubbles (User vs Assistant)
- Left sidebar for chat history
- Sticky input bar
- Fully responsive layout

### 7️ Safety Guardrails
- Explicitly blocks:
  - Buy/sell advice
  - Stock tips
  - Guaranteed returns
- Enforces:
  - Educational tone
  - Neutral explanations
- Displays a clear disclaimer in the UI

##  Application Workflow

### 1️ User Interaction
- User types a message or uploads a PDF
- Each conversation is assigned a unique `session_id`

### 2️ Intent Classification
Each user message is classified into one of the following categories:
- **Investment Coach**
- **Market Commentary**
- **Restricted (Blocked)**

This ensures safety and prevents financial advice or stock recommendations.

### 3️ Context Retrieval (RAG)
If PDFs exist for the current session:
- Relevant document chunks are retrieved from **FAISS**
- Retrieved context is injected into the LLM prompt

This enables document-grounded, accurate responses.

### 4️ LLM Response Generation
- LangChain sends the augmented prompt (user query + retrieved context) to the LLM
- The model generates a **safe, grounded, and educational response**
  
### 5️ Memory & Resume Chat
- User and assistant messages are stored per session
- Previous chats appear in a sidebar
- Clicking a chat restores its complete history

##  Tech Stack

### 🔹 Backend
- **FastAPI** – API framework
- **LangChain (Runnable API)** – LLM orchestration
- **OpenAI Models** – Text generation & embeddings
- **FAISS** – Vector database for RAG
- **python-multipart** – File upload handling

###  Frontend
- **HTML**
- **CSS** (Flexbox, Dark UI)
- **Vanilla JavaScript**

##  Key Highlights
- RAG-based PDF Question Answering
- Session-based memory with resume chat
- Intent classification and safety guardrails
- Clean ChatGPT-style UI
- Production-ready architecture

  ## Live Demo
  
![Live Demo](https://github.com/Narendra8767/investment-coach/blob/main/Live%20Demo.png)

## Observability & Monitoring with LangSmith

### LangSmith Integration

This project integrates **LangSmith** for LLM observability, tracing, and debugging during development.

LangSmith is used to:
- Monitor **LangChain executions**
- Trace **prompt → model → response** flows
- Debug **latency issues, failures, and unexpected outputs**
- Improve **prompt quality** and overall system reliability

This observability layer helps ensure the chatbot behaves **predictably and safely**, especially when combining:
- User input
- PDF-based RAG context
- Live market news data

  ## LangSmith
  
![LangSmith](<img width="1672" height="943" alt="Langsmith" src="https://github.com/user-attachments/assets/69a8cb8c-9b2d-4334-b034-6d26979f2092" />
)


