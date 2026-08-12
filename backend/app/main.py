from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.candidate_context import CandidateContextService
from app.api.chat import router as chat_router

candidate_context_service = CandidateContextService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    candidate_context_service.load()

    app.state.candidate_context_service = candidate_context_service

    yield


app = FastAPI(
    title="AI Recruiter Assistant",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "AI Recruiter Assistant API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }