from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from urllib.parse import urlparse
from app.services.github import (
    get_repository,
    get_repository_tree,
    get_important_files,
    get_file_content,
)
from app.analyzers.technology import (
    detect_technologies,
    detect_package_technologies,
)
from app.analyzers.technology import detect_technologies


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
        important_files = get_important_files(
        tree_data.get("tree", []))
        technologies = detect_technologies(important_files)
        if "package.json" in important_files:
            package_content = await get_file_content(
                owner,
                repository,
                "package.json",
            )
        
            package_technologies = detect_package_technologies(
                package_content
            )
        
            technologies = sorted(
                set(technologies + package_technologies)
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
    "important_files": important_files,
    "technologies": technologies,
}