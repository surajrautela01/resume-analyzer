AI Resume Analyzer

An AI-powered Resume Screening system that compares a candidate’s resume with a Job Description (JD) and decides whether the candidate should be shortlisted or rejected.

🧠 How it Works (LangChain + Cohere Pipeline)

When a resume is uploaded, the system uses LangChain + Cohere to understand and compare the resume with the Job Description.

📄 1. Resume Processing
PDF resume is uploaded by the user
PyPDFLoader extracts text from the resume
Text is broken into smaller chunks using RecursiveCharacterTextSplitter
🔍 2. Embeddings (Cohere)
Each text chunk is converted into vectors using Cohere Embeddings
Helps system understand meaning, not just keywords

👉 Enables semantic search instead of keyword matching

📦 3. Vector Storage (FAISS)
Resume chunks are stored in FAISS vector database
Allows fast retrieval of relevant sections based on JD
📌 4. Similarity Search
Job Description is also converted into embeddings
FAISS finds most relevant resume sections
🤖 5. LLM Analysis (Cohere Chat Model)
Relevant resume + JD context is sent to Cohere LLM
Acts like a strict recruiter
Evaluates:
Skills match
Missing skills
Experience gaps
Overall fit
📊 6. Final Output
Match Score
Verdict (REJECTED / SHORTLISTED)
Missing Skills
Reasoning
⚡ Tech Stack
Python
FastAPI (Backend)
Streamlit (Frontend)
LangChain
Cohere LLM + Embeddings
FAISS
