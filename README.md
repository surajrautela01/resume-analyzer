📄 AI Resume Analyzer

AI Resume Analyzer is an AI-powered project that compares a candidate’s resume with a Job Description (JD) and decides whether the candidate should be shortlisted or rejected.

🧠 How It Works (LangChain + Cohere Pipeline)

When a resume is uploaded, the system uses LangChain and Cohere to understand and compare the resume with the Job Description.

📄 1. Resume Processing
A PDF resume is uploaded by the user.
PyPDFLoader extracts text from the resume.
The extracted text is split into smaller chunks using RecursiveCharacterTextSplitter.
🔍 2. Embeddings (Cohere)
Each text chunk is converted into embeddings using Cohere Embeddings.
This helps the system understand the meaning of the text instead of just keywords.

👉 This enables semantic search instead of simple keyword matching.

📦 3. Vector Storage (FAISS)
All resume chunks are stored in a FAISS vector database.
FAISS allows fast and efficient similarity search.
📌 4. Similarity Search
The Job Description is also converted into embeddings.
FAISS retrieves the most relevant parts of the resume that match the JD.
🤖 5. LLM Analysis (Cohere Chat Model)
Relevant resume context and JD are sent to the Cohere LLM.
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
⚡ Tech Stack
Python
FastAPI (Backend)
Streamlit (Frontend)
LangChain
Cohere (Embeddings + LLM)
FAISS (Vector Database)