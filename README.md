# COLD_MAIL_GENERATOR
🚀 Cold Email Generator using LangChain + Groq + Streamlit

This project is an AI-powered Cold Email Generator that automatically extracts job postings from a company’s careers webpage and generates a personalized cold email tailored to the job role.
It uses LangChain, Groq LLM (LLaMA 3.1), Streamlit, and a vector database (ChromaDB) for portfolio matching.

📌 Features

🌐 Scrapes job descriptions directly from a careers webpage

🧠 Uses Groq LLM (LLaMA 3.1) to extract structured job data

📄 Extracts:

Job Role

Experience

Skills

Description

✉️ Generates a professional cold email as a Business Development Executive

🔗 Automatically attaches relevant portfolio links using vector similarity search

🎨 Simple and clean Streamlit UI

| Component | Technology                    |
| --------- | ----------------------------- |
| LLM       | Groq (LLaMA 3.1 – 8B Instant) |
| Framework | LangChain                     |
| Frontend  | Streamlit                     |
| Vector DB | ChromaDB                      |
| Data      | CSV-based portfolio           |
| Language  | Python                        |

.
├── app.py                  # Streamlit application entry point
├── chain.py                # LLM chains (job extraction + email writing)
├── Portfolio.py            # Portfolio vector store logic
├── utils.py                # Text cleaning utilities
├── resources/
│   └── my_portfolio.csv    # Portfolio data (Techstack + Links)
├── vectorstore/            # ChromaDB persistent storage
├── .env                    # Environment variables
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
