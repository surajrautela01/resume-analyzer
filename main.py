import os
import tempfile
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from dotenv import load_dotenv

# Modern Imports for Python 3.14
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()
app = FastAPI(title="Strict AI Resume Analyzer")

@app.post("/analyze")
async def analyze_resume(jd_text: str = Form(...), file: UploadFile = File(...)):
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="COHERE_API_KEY missing in .env")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        # 1. Extraction & Chunking
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
        splits = text_splitter.split_documents(docs)

        # 2. Vector DB (Retrieving Context)
        embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=api_key)
        vectorstore = FAISS.from_documents(splits, embeddings)
        relevant_docs = vectorstore.similarity_search(jd_text, k=4)
        context_text = "\n\n".join([doc.page_content for doc in relevant_docs])

        # 3. LLM with Aggressive Penalty Logic
        llm = ChatCohere(model="command-r-08-2024", cohere_api_key=api_key)

        prompt = f"""
        You are a CRITICAL Technical Recruiter. Your task is to find reasons to REJECT the candidate if they don't meet the JD.
        
        RESUME CONTEXT:
        {context_text}
        
        JOB DESCRIPTION:
        {jd_text}
        
        STRICT SCORING RULES:
        1. If a core skill (like DevOps, FastAPI, etc.) is mentioned in JD but missing in Resume, deduct 20 points immediately.
        2. If the total score is less than 70, the Verdict MUST be 'REJECTED'.
        3. Do NOT mention 'potential', 'enthusiasm', or 'future growth'. Only judge on existing skills.
        4. If the candidate has 0 years of experience but the JD asks for experience, deduct 30 points.
        
        Format your response exactly like this:
        MATCH SCORE: [0-100]%
        VERDICT: [REJECTED or SHORTLIST]
        MISSING SKILLS: [List of skills]
        REASONING: [Strict 1-line explanation]
        """
        
        response = llm.invoke(prompt)
        return {"status": "success", "analysis": response.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(tmp_path): os.remove(tmp_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
 