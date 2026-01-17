from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import os
from app.chains import run_chat
from fastapi import UploadFile, File
from app.rag import process_pdf
from app.sessions import add_vectorstore
import uuid

from app.memory import (
    create_chat,
    add_message,
    get_chat,
    list_chats
)

app = FastAPI(title="Investment Coach Assistant")


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Serve frontend assets
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")

from app.database import init_db

@app.on_event("startup")
def startup():
    init_db()

class ChatRequest(BaseModel):
    message: str
    session_id: str

@app.post("/chat")
def chat(req: ChatRequest):
    if req.session_id not in [c["session_id"] for c in list_chats()]:
        create_chat(req.session_id, req.message[:30])

    add_message(req.session_id, "user", req.message)
    reply = run_chat(req.message, req.session_id)
    add_message(req.session_id, "assistant", reply)

    return {"reply": reply}



@app.post("/upload-pdf")
def upload_pdf(session_id: str, file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())

    vectorstore = process_pdf(path)
    add_vectorstore(session_id, vectorstore)

    return {"status": "PDF uploaded and indexed"}


@app.get("/chats")
def get_chats():
    return list_chats()

@app.get("/chat/{session_id}")
def load_chat(session_id: str):
    return get_chat(session_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
