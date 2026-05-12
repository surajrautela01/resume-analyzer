When a resume is uploaded, the system uses LangChain + Cohere to understand and compare the resume with the Job Description.

📄 1. Resume Processing
PDF resume is uploaded by the user
PyPDFLoader extracts text from the resume
Text is broken into smaller chunks using RecursiveCharacterTextSplitter
🔍 2. Embeddings (Cohere)
Each text chunk is converted into vectors using Cohere Embeddings
These embeddings help the system understand meaning, not just keywords

👉 This allows semantic matching (not just simple text matching)

📦 3. Vector Storage (FAISS)
All resume chunks are stored in FAISS vector database
FAISS helps quickly search most relevant parts of resume based on JD
📌 4. Similarity Search
Job Description (JD) is also converted into embedding
FAISS finds top matching resume sections related to JD
🤖 5. LLM Analysis (Cohere Chat Model)
Relevant resume + JD is sent to Cohere Chat LLM
LLM acts like a strict recruiter
It evaluates:
Skill match
Missing skills
Experience gaps
Overall fit
📊 6. Final Output

LLM returns:

Match Score
Verdict (REJECTED / SHORTLISTED)
Missing Skills
Reasoning
⚡ Simple summary

👉 LangChain = pipeline builder (connects all steps)
👉 Cohere Embeddings = understands meaning of text
👉 FAISS = fast similarity search engine
👉 Cohere LLM = final decision maker (recruiter brain)