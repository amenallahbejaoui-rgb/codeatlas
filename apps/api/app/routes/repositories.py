from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from urllib.parse import urlparse
from app.services.github import get_repository, get_repository_tree


router = APIRouter(prefix="/api/repositories", tags=["repositories"])

class RepositoryRequest(BaseModel):
    url: str


@router.post("/analyze")
async def analyze_repository(request: RepositoryRequest):
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

    try:
        github_data = await get_repository(owner, repository)
        default_branch = github_data.get("default_branch")

        tree_data = await get_repository_tree(
        owner,
        repository,
        default_branch,
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found.",
        )

    return {
    "owner": owner,
    "repository": repository,
    "description": github_data.get("description"),
    "stars": github_data.get("stargazers_count"),
    "language": github_data.get("language"),
    "default_branch": default_branch,
    "tree": tree_data.get("tree", []),
}
