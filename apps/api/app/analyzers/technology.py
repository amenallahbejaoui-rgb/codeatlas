import json
def detect_technologies(files: list[str]):
    technologies = set()

    for file in files:
        filename = file.split("/")[-1].lower()
        path = file.lower()

        # Frontend
        if filename.endswith((".html", ".css", ".js", ".jsx", ".ts", ".tsx")):
            technologies.add("Frontend")

        # Python
        if filename.endswith(".py"):
            technologies.add("Python")

        # Java
        if filename.endswith(".java"):
            technologies.add("Java")

        # PHP
        if filename.endswith(".php"):
            technologies.add("PHP")

        # Database
        if filename.endswith(".sql"):
            technologies.add("Database")

        # Node.js / JavaScript ecosystem
        if filename == "package.json":
            technologies.add("Node.js")

        # Python web frameworks
        if filename in ("requirements.txt", "pyproject.toml"):
            technologies.add("Python")

        # Docker
        if filename == "dockerfile" or "docker-compose" in filename:
            technologies.add("Docker")

        # CI/CD
        if ".github/workflows/" in path:
            technologies.add("CI/CD")

        # Testing
        if (
            "test" in path
            or "tests" in path
            or "cypress" in filename
            or "jest" in filename
        ):
            technologies.add("Testing")

    return sorted(technologies)
def detect_package_technologies(package_content: str):
    technologies = set()

    try:
        package = json.loads(package_content)
    except json.JSONDecodeError:
        return []

    dependencies = {
        **package.get("dependencies", {}),
        **package.get("devDependencies", {}),
    }

    technology_map = {
        "react": "React",
        "react-dom": "React",
        "next": "Next.js",
        "vue": "Vue.js",
        "nuxt": "Nuxt.js",
        "angular": "Angular",
        "express": "Express",
        "fastify": "Fastify",
        "nestjs": "NestJS",
        "cypress": "Cypress",
        "jest": "Jest",
        "eslint": "ESLint",
        "prettier": "Prettier",
        "tailwindcss": "Tailwind CSS",
        "typescript": "TypeScript",
    }

    for dependency in dependencies:
        if dependency in technology_map:
            technologies.add(technology_map[dependency])

    return sorted(technologies)
if __name__ == "__main__":
    package_content = """
    {
        "dependencies": {
            "react": "^18.0.0",
            "next": "^14.0.0",
            "express": "^4.0.0"
        },
        "devDependencies": {
            "cypress": "^12.0.0",
            "typescript": "^5.0.0"
        }
    }
    """

    print(detect_package_technologies(package_content))
