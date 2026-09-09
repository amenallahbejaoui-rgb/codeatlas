def detect_architecture(technologies: list[str], files: list[str]):
    architecture = set()

    technology_set = set(technologies)
    file_set = set(files)

    # Frontend
    frontend_technologies = {
        "Frontend",
        "React",
        "Next.js",
        "Vue.js",
        "Nuxt.js",
        "Angular",
        "Tailwind CSS",
    }

    if technology_set & frontend_technologies:
        architecture.add("Frontend")

    # Backend
    backend_technologies = {
        "Express",
        "Fastify",
        "NestJS",
        "FastAPI",
        "Django",
        "Flask",
        "Laravel",
    }

    if technology_set & backend_technologies:
        architecture.add("Backend")

    # Database
    database_technologies = {
        "Database",
        "PostgreSQL",
        "MySQL",
        "MongoDB",
        "SQLite",
        "Redis",
    }

    if technology_set & database_technologies:
        architecture.add("Database")

    # AI
    ai_technologies = {
        "TensorFlow",
        "PyTorch",
        "Transformers",
        "Scikit-learn",
        "OpenAI",
    }

    if technology_set & ai_technologies:
        architecture.add("AI")

    # Authentication
    auth_indicators = {
        "auth",
        "authentication",
        "login",
        "jwt",
        "passport",
        "oauth",
    }

    for file in file_set:
        filename = file.lower()

        if any(indicator in filename for indicator in auth_indicators):
            architecture.add("Authentication")
            break

    # Testing
    testing_technologies = {
        "Testing",
        "Cypress",
        "Jest",
        "Pytest",
    }

    if technology_set & testing_technologies:
        architecture.add("Testing")

    # CI/CD
    if "CI/CD" in technology_set:
        architecture.add("CI/CD")

    # Cloud / deployment
    cloud_indicators = {
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "vercel.json",
        "netlify.toml",
        "render.yaml",
        "fly.toml",
    }

    if any(
        file.lower().split("/")[-1] in cloud_indicators
        for file in file_set
    ):
        architecture.add("Cloud / Deployment")

    return sorted(architecture)