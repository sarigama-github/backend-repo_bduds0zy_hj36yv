from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os

from database import create_document, get_documents
from schemas import Score

app = FastAPI(title="Road Runner API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.get("/test")
def test():
    database_url = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
    database_name = os.getenv("DATABASE_NAME", "appdb")
    return {
        "backend": "ok",
        "database": "mongo",
        "database_url": database_url,
        "database_name": database_name,
        "connection_status": "unknown in test endpoint",
        "collections": [],
    }


class ScoreIn(BaseModel):
    player: str = "Guest"
    distance: float


@app.post("/scores")
def save_score(payload: ScoreIn):
    doc_id = create_document("score", payload.model_dump())
    return {"id": doc_id, "status": "saved"}


@app.get("/scores")
def list_scores(limit: int = 20):
    results = get_documents("score", limit=limit)
    # sort by distance desc if available
    results = sorted(results, key=lambda x: x.get("distance", 0), reverse=True)
    return results
