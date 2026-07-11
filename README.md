# 🤖 F.R.I.D.A.Y. AI Assistant

> **F.R.I.D.A.Y. (Female Replacement Intelligent Digital Assistant Youth)** is a personal AI assistant inspired by Marvel's *F.R.I.D.A.Y.*, designed to evolve into a modular AI operating system capable of understanding, remembering, and assisting users with everyday digital tasks.
> 🚧 **Status:** Actively under development. New features are being added milestone by milestone following semantic versioning.

> **Current Version:** `v0.1.0 - Core AI Assistant`

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 📌 Overview

F.R.I.D.A.Y. aims to become a fully featured AI assistant with capabilities such as:

* 🧠 Long-term memory
* 📄 Document understanding (RAG)
* 🎤 Voice interaction
* 💻 Computer automation
* 🌐 Browser automation
* 👁️ Vision capabilities
* 🤖 Multi-agent architecture

Version **0.1.0** focuses on building the core conversational AI system.

---

# ✨ Features (v0.1.0)

- 🤖 AI-powered conversational assistant using Google Gemini
- 🧠 Short-term conversation memory
- 🎭 Custom F.R.I.D.A.Y. personality
- ⚡ FastAPI REST API backend
- 📝 Request and response logging
- 🛡 Professional error handling
- 🔐 Secure API key management using `.env`
- 📦 Modular project architecture
- 💬 Context-aware conversations within the current session

# ✅ Current Capabilities

- Remembers conversations during the current session
- Maintains a consistent F.R.I.D.A.Y. personality
- Generates responses using Google Gemini
- Logs every AI request and response
- Handles AI service failures gracefully

# 🎯 Example Conversation

User:
> My name is Stavan.

F.R.I.D.A.Y.:
> Nice to meet you, Stavan.

User:
> What is my name?

F.R.I.D.A.Y.:
> Your name is Stavan.

---

# 🛠️ Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Core programming language |
| FastAPI             | Backend API               |
| Google Gemini API   | AI Model & Inference      |
| Pydantic            | Data Validation           |
| python-dotenv       | Environment Variables     |
| Logging             | Monitoring & Debugging    |
| Uvicorn             | ASGI server               |
| Git & GitHub        | Version control           |

---

# 📁 Project Structure

```text
friday-ai/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── memory.py
│   │
│   ├── models/
│   │
│   ├── prompts/
│   │   └── system_prompt.py
│   │
│   ├── services/
│   │   └── chat_service.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

# 🏗️ Architecture

```text
User
   │
   ▼
FastAPI
   │
   ▼
Chat Service
   │
   ├── System Prompt
   ├── Memory
   ├── Logger
   ▼
Google Gemini API
```
---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Strocks1892/friday-ai.git
cd friday-ai
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 5. Start the Server

```bash
uvicorn app.main:app --reload
## 📖 API Documentation

Once the server is running:

Swagger UI

http://127.0.0.1:8000/docs

ReDoc

http://127.0.0.1:8000/redoc
```

---

# 📌 Roadmap

## ✅ v0.1.0 - Core AI Assistant

- [x] FastAPI Backend
- [x] Google Gemini Integration
- [x] Custom F.R.I.D.A.Y. Personality
- [x] Short-Term Memory
- [x] Logging
- [x] Error Handling
- [x] Modular Project Structure

---

## 🚧 v0.2.0 - AI Tools

- [ ] Tool Calling
- [ ] Calculator
- [ ] Date & Time
- [ ] Weather
- [ ] Browser Search
- [ ] File Search
- [ ] Application Launcher

---

## 🔜 v0.3.0 - Voice Assistant

- [ ] Speech-to-Text
- [ ] Text-to-Speech
- [ ] Wake Word

---

## 🔜 v0.4.0 - Vision

- [ ] OCR
- [ ] Image Understanding
- [ ] Screenshot Analysis

---

## 🔜 v0.5.0 - Long-Term Memory

- [ ] User Preferences
- [ ] Database
- [ ] Vector Memory
- [ ] Retrieval-Augmented Generation (RAG)

---

## 🔜 v0.6.0 - Computer Automation

- [ ] Browser Automation
- [ ] File Management
- [ ] Computer Control
- [ ] Terminal Automation

---

## 🎯 v1.0.0

- [ ] Fully Modular AI Assistant
- [ ] Persistent Memory
- [ ] Voice + Vision + Automation
- [ ] Production Ready

---

# 📦 Version History

## v0.1.0 - Core AI Assistant

**Release Date:** July 2026

### ✨ Added

- FastAPI backend
- Google Gemini integration
- Custom F.R.I.D.A.Y. personality
- Short-term conversation memory
- Professional logging
- Error handling
- Modular project architecture
- Environment-based configuration

### 🛠 Improved

- Cleaner project structure
- Better prompt engineering
- More consistent AI responses

### 🐞 Fixed

- Gemini model compatibility issues
- Chat service initialization
- Conversation memory handling
- Logging improvements

---

# 📚 Learning Goals

This project is being built to explore:

* AI Engineering
* Large Language Models
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* AI Agents
* Backend Development
* Software Architecture
* FastAPI
* Git & GitHub
* Docker
* Deployment

---

# 🤝 Contributing

Contributions, suggestions, and discussions are welcome. Feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Future Vision

The long-term goal is to transform F.R.I.D.A.Y. into a modular AI operating system capable of understanding context, remembering users, controlling local applications, interacting with the web, analyzing documents, processing voice and images, and assisting with coding, research, productivity, and everyday digital workflows while maintaining a scalable and production-ready architecture.

---

**Built with ❤️ using Python and AI.**
