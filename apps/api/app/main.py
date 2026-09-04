from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.repositories import router as repositories_router


app = FastAPI(
    title="CodeAtlas API",
    description="Backend API for analyzing GitHub repositories.",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(repositories_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}