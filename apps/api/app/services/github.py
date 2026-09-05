import httpx


async def get_repository(owner: str, repository: str):
    url = f"https://api.github.com/repos/{owner}/{repository}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    response.raise_for_status()

    return response.json()


async def get_repository_tree(owner: str, repository: str, branch: str):
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository}/git/trees/{branch}"
        "?recursive=1"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    response.raise_for_status()

    return response.json()