📄 AI Resume Analyzer

AI Resume Analyzer is an AI-powered project that compares a candidate’s resume with a Job Description (JD) and decides whether the candidate should be shortlisted or rejected.

🧠 How It Works (LangChain + Cohere Pipeline)

When a resume is uploaded, the system uses LangChain and Cohere to understand and compare the resume with the Job Description.

📄 1. Resume Processing
A PDF resume is uploaded by the user.
PyPDFLoader extracts text from the resume.
The text is split into smaller chunks using RecursiveCharacterTextSplitter.


































🔍 2. Embeddings (Cohere)
Each text chunk is converted into embeddings using Cohere Embeddings.
This helps the system understand meaning instead of just keywords.

👉 Enables semantic matching instead of keyword matching.














📦 3. Vector Storage (FAISS)
All resume chunks are stored in a FAISS vector database.
FAISS enables fast similarity search based on Job Description.























📌 4. Similarity Search
Job Description is also converted into embeddings.
FAISS retrieves the most relevant resume sections matching the JD.










🤖 5. LLM Analysis (Cohere Chat Model)
Relevant resume context + JD is sent to Cohere LLM.
The model acts like a strict technical recruiter.
It evaluates:
Skill match
Missing skills
Experience gaps
Overall suitability
📊 6. Final Output

The model returns:

Match Score (0–100%)
Verdict: REJECTED / SHORTLISTED
Missing Skills
Reasoning




⚙️ How to Run the Project

1. Create .env file

Create a .env file in the root directory and add your Cohere API key:

COHERE_API_KEY=your_cohere_api_key_here

👉 You can create your API key from: https://dashboard.cohere.com/







2. Run Backend (FastAPI)
uvicorn main:app --reload --port 8001
3. Run Frontend (Streamlit)
streamlit run app.py









⚡ Tech Stack










Python
FastAPI (Backend)






























Streamlit (Frontend)
LangChain
Cohere (Embeddings + LLM)
FAISS (Vector Database)
