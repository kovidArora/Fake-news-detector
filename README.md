#  Fake News Detector (RAG + Llama 3)

An AI-powered fake news detection system built using **Retrieval Augmented Generation (RAG)** and **Llama 3**.

The application retrieves related news articles using **NewsAPI**, stores them in a vector database using **FAISS**, and uses an LLM to analyze whether a claim is **REAL, FAKE, or UNVERIFIED**.

Built with:
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Llama 3
- NewsAPI


##  Features

###  AI Based Fact Checking
- Uses Llama 3 to analyze claims
- Provides:
  - Classification
  - Confidence score
  - Explanation
  - Key reasoning points


###  RAG Pipeline

Instead of relying only on the LLM:

```
User Input
    |
    v
NewsAPI Search
    |
    v
Relevant Articles
    |
    v
FAISS Vector Database
    |
    v
Similarity Retrieval
    |
    v
Llama 3 Analysis
    |
    v
Result
```


###  Output

Example:

```
Prediction:
 FAKE

Confidence:
85%

Why?

No credible sources support the claim.

Key Points:
• No matching reports found
• Claim contradicts available evidence
```


##  Tech Stack

| Component | Technology |
|-|-|
| Frontend | Streamlit |
| LLM | Llama 3 |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace Sentence Transformers |
| News Retrieval | NewsAPI |
| Deployment | Streamlit Cloud |


##  Project Structure

```
Fake-News-Detector/

│
├── app.py                 # Streamlit application
│
├── llm/
│   ├── detector.py        # LLM classification logic
│   └── llama.py           # Llama model setup
│
├── rag/
│   ├── news_loader.py     # Fetch news articles
│   ├── vector_store.py    # Create FAISS database
│   └── retriever.py       # Retrieve relevant context
│
├── requirements.txt
├── .env.example
└── README.md
```


##  Installation

Clone repository:

```bash
git clone <your-repository-link>

cd Fake-News-Detector
```


Create virtual environment:

```bash
python -m venv venv
```


Activate:

Windows:

```bash
venv\Scripts\activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


##  Environment Variables

Create a `.env` file:

```
NEWS_API_KEY=your_news_api_key
GROQ_API_KEY=your_llama_api_key
```


## ▶️ Run Locally

Start Streamlit:

```bash
streamlit run app.py
```


Open:

```
http://localhost:8501
```


##  How It Works

1. User enters a news claim.

2. The system extracts keywords.

3. NewsAPI searches for related articles.

4. Articles are converted into embeddings.

5. FAISS finds the most relevant evidence.

6. Llama 3 analyzes:
   - supporting evidence
   - contradicting evidence
   - lack of evidence

7. Final response is generated.


##  Limitations

- NewsAPI only provides recent news.
- Confidence score is LLM-estimated.
- Lack of evidence does not always mean false.
- The system depends on available sources.


## Future Improvements

- Add source credibility scoring
- Add article URL input
- Add web scraping
- Add evaluation dashboard
- Compare RAG vs normal LLM accuracy
- Add persistent vector database
- Add user history


## Author

Kovid Arora