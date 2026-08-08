from fastapi import FastAPI


app = FastAPI(
    title="AI Recruiter Assistant",
    version="1.0.0"
)


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

