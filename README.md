# PyBot – AI Chat Assistant

**Author:** Meeraj Krishna  
**Language:** Python  
**Version:** 1.0.0  

PyBot is a simple and interactive chatbot built using **Gradio** and **OpenAI’s ChatCompletion API**.  
It allows users to chat with an AI assistant that specializes in **Python programming and problem solving**.

---

## 🧠 Features

- 💬 Chat with an AI trained for Python programming help  
- 🔐 Secure API key handling via environment variable  
- 🌐 Web interface powered by **Gradio**  
- ⚡ Real-time responses using **OpenAI GPT models**  
- 🧰 Modular and beginner-friendly code structure  

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

Make sure you have Python 3.8+ installed, then run:

```bash
pip install openai gradio
```

---

### 2️⃣ Set Up Your OpenAI API Key

Before running the app, set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key_here"    # macOS/Linux
setx OPENAI_API_KEY "your_api_key_here"      # Windows
```

---

### 3️⃣ Run the App

```bash
python Pybot.py
```

Once running, Gradio will open a local web interface (usually at  
`http://127.0.0.1:7860/`) where you can start chatting with the bot.

---

## 🧩 Code Overview

The core of **PyBot** lies in these components:

- **`CustomChatGPT()`** — Sends user input to OpenAI’s API and retrieves responses  
- **`messages[]`** — Stores the chat history between user and assistant  
- **`gr.Interface()`** — Builds the chat UI with Gradio  

---

## 🖼️ Example Output

```
User: What is a Python decorator?
Bot: A decorator in Python is a function that modifies another function...
```

---

## 🧑‍💻 Author

**Meeraj Krishna**  
💡 Python Developer | AI Enthusiast  

> “Code smarter, not harder — let AI assist you.”

---

## 📜 License

This project is open-source and free to use for educational purposes.
