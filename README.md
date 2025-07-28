# 🤖 Local AI Agent using LangChain

This project implements a **Local AI Agent** that can understand and respond to queries based on restaurant reviews. It's built using Python, LangChain, and ChromaDB for local vector storage — no cloud APIs required!

---

## 🧠 Features

- Load and embed custom CSV documents (e.g., restaurant reviews)
- Store and search embeddings using **Chroma** vector database
- Fast local inference with no external dependencies
- Clean modular code: `utils.py`, `vector.py`, `main.py`

---

## 📁 Project Structure
Local_AI_Agent/
├── chrome_langchain_db/ # Local Chroma vector store
├── realistic_restaurant_reviews.csv
├── main.py # Entry point for the app
├── vector.py # Vector store setup
├── utils.py # Supporting utility functions
├── requirements.txt # Python dependencies
└── README.md # This file

---

## 🚀 How to Run

### 1. Install dependencies
Make sure you have Python 3.8+ installed. Then run:

```bash
pip install -r requirements.txt

2. Run the main script
bash
Copy code
python main.py
The script will check for the Chroma vector store. If it doesn’t exist, it will create one using the reviews in the CSV file.

🛠 Technologies Used
Python 🐍

LangChain

ChromaDB

VS Code

To Do (Future Improvements)
Add GUI with Streamlit or Tkinter

Add support for multiple document types (PDF, TXT)

Implement better query parsing and response generation

👤 Author
Govardhan Reddy Mudupu
GitHub Profile: govardhanreddy2804
