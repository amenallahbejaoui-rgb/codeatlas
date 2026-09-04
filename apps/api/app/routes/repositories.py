from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from urllib.parse import urlparse


router = APIRouter(prefix="/api/repositories", tags=["repositories"])


class RepositoryRequest(BaseModel):
    url: str


@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):
    parsed_url = urlparse(request.url)

    if parsed_url.hostname != "github.com":
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid GitHub repository URL.",
        )

    parts = parsed_url.path.strip("/").split("/")

    if len(parts) < 2:
        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub repository URL.",
        )

    owner = parts[0]
    repository = parts[1].removesuffix(".git")

    return {
        "owner": owner,
        "repository": repository,
    }