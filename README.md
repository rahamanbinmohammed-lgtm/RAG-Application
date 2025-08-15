# 🧠 TeckyBot: News Research & Q&A Tool

TeckyBot is a Streamlit-based web app that lets users input any **two article URLs**, extracts the full text from those sites, and allows users to ask **natural language questions** about the content. Powered by **Google's Gemini 1.5 Flash** model, it ensures answers are strictly based on the provided context.

---

## 🚀 Features

- 🌐 **Web scraping** from any two public URLs using `requests` and `BeautifulSoup`
- 🤖 **Question-answering** based on the scraped content using Gemini API
- 🧾 Simple UI built with **Streamlit**
- 💬 Context-aware responses without external assumptions
- ⚡ Instant setup and lightweight

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/teckybot.git
cd teckybot
````

### 2. Install dependencies

Make sure you have Python 3.8+

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

You need a **Google Gemini API key**. You can get it from [Google AI Studio](https://makersuite.google.com/app).

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Uncomment `load_dotenv()` and relevant code in `app.py` to use it securely.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Your browser will open the app at `http://localhost:8501/`.

---

## 📄 Usage

1. Input two URLs in the sidebar (default examples are provided).
2. Click **"Process URLs"** to scrape and store data.
3. Ask a question in the main input field.
4. Click **"Get Answer"** to receive a context-based response.

---

## 📁 File Structure

```
.
├── app.py                # Main Streamlit app
├── extracted_data.txt    # Text extracted from URLs (generated)
├── requirements.txt      # Dependencies
├── .env                  # API Key (not committed)
└── README.md             # Project documentation
```

---

## ⚠️ Security Note

The current version includes a hardcoded API key — **do not commit this in production**. Use `.env` for secure management.

---

## 🧠 Tech Stack

* Python
* Streamlit
* BeautifulSoup
* Requests
* Google Generative AI (Gemini API)

---

## 💡 Future Improvements

* Use real **vector databases** (e.g. FAISS or Chroma) for efficient context handling
* Support **multiple URLs or documents**
* Add **text chunking** and **semantic search** before sending to Gemini
* Deploy to **Streamlit Cloud**, **Hugging Face Spaces**, or use **LocalTunnel**

---

## 📜 License

MIT License

---

## 🙌 Author

**Mohammed Abdul Rahaman**

---

```

---

Let me know if you'd like to add deployment instructions (e.g. for Streamlit Cloud) or convert it into a GitHub-friendly template with badges!
```
