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

---

##  Disclaimer

> **This chatbot is strictly for educational purposes only.**  
> It does **not** provide financial advice, stock recommendations, buy/sell signals, or guarantees of returns.

---

## ✨ Key Features

### 1️ Investment Coach Mode
- Explains core investment concepts such as:
  - SIP
  - Mutual Funds
  - Risk
  - Diversification
- Uses **simple language and real-world analogies**
- Avoids any form of buy/sell recommendations
- Supports **PDF-based RAG grounding** when documents are uploaded

---

### 2️ Market Commentary Mode
- Provides **neutral explanations** of market movements
- Uses **live business and market news**
- No predictions or investment advice
- Focuses on **macroeconomic reasoning and context**

---

### 3️ RAG-Based PDF Question Answering
- Users can upload PDFs directly during chat
- PDFs are:
  - Parsed
  - Chunked
  - Embedded
  - Stored in a vector database (FAISS)
- Relevant chunks are retrieved for each user query
- LLM responses are **fully grounded in uploaded documents**

---

### 4️ Upload PDF During Chat
- Upload PDFs at any point in a conversation using the ➕ button
- Multiple PDFs supported per session
- Each chat session maintains its **own document context**
- Enables questions like:
  - *“Summarize the PDF I uploaded”*
  - *“Explain the risk factors mentioned in the document”*

---

### 5️ Resume Chat (Session Persistence)
- Each chat has a unique `session_id`
- Previous chats appear in a **left sidebar**
- Users can:
  - Resume old chats
  - Start new chats
- Chat history is restored automatically on reload

---

### 6️ UI & Styling
- Modern **dark theme**
- ChatGPT-style message bubbles (User vs Assistant)
- Left sidebar for chat history
- Sticky input bar
- Fully responsive layout

---

### 7️ Safety Guardrails
- Explicitly blocks:
  - Buy/sell advice
  - Stock tips
  - Guaranteed returns
- Enforces:
  - Educational tone
  - Neutral explanations
- Displays a clear disclaimer in the UI

---



