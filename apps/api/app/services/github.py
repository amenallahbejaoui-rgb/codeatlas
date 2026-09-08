import httpx
import base64
import asyncio

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

def get_important_files(tree: list):
    important_files = []

    ignored_folders = {
        "node_modules",
        ".git",
        ".next",
        "dist",
        "build",
        "__pycache__",
        ".venv",
        "venv",
        "coverage",
    }

    important_extensions = {
        ".py",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".java",
        ".php",
        ".go",
        ".rs",
        ".cs",
        ".sql",
        ".json",
        ".yml",
        ".yaml",
        ".toml",
        ".xml",
    }

    important_names = {
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "requirements.txt",
        "package.json",
        "README.md",
        "Makefile",
    }

    for item in tree:
        if item["type"] != "blob":
            continue

        path = item["path"]

        parts = path.split("/")

        if any(folder in ignored_folders for folder in parts):
            continue

        filename = parts[-1]

        if (
            filename in important_names
            or any(filename.endswith(extension) for extension in important_extensions)
        ):
            important_files.append(path)

    return important_files

async def get_file_content(owner: str, repository: str, path: str):
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository}/contents/{path}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    response.raise_for_status()

    data = response.json()
    content = data.get("content", "")

    return base64.b64decode(content).decode("utf-8")




async def test():
    print("Starting test...")

    content = await get_file_content(
        "saurabhdaware",
        "text-to-handwriting",
        "package.json",
    )

    print("Got package.json!")
    print(content[:1000])


if __name__ == "__main__":
    asyncio.run(test())