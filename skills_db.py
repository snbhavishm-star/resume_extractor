"""
Master skills database used to detect skills mentioned anywhere in a resume,
even if they aren't neatly listed under a 'Skills' heading.
Organized by category so the output can group skills meaningfully.
"""

SKILLS_DB = {
    "Programming Languages": [
        "python", "java", "c++", "c#", "javascript", "typescript", "go", "golang",
        "rust", "kotlin", "swift", "php", "ruby", "r", "matlab", "scala", "perl",
        "c", "dart", "sql", "bash", "shell scripting", "julia"
    ],
    "Web & Frontend": [
        "html", "css", "react", "reactjs", "react.js", "angular", "vue", "vue.js",
        "next.js", "nextjs", "svelte", "tailwind", "tailwindcss", "bootstrap",
        "jquery", "redux", "webpack", "sass", "scss", "material ui", "chakra ui"
    ],
    "Backend & Frameworks": [
        "node.js", "nodejs", "express", "express.js", "django", "flask", "fastapi",
        "spring", "spring boot", "asp.net", ".net", "ruby on rails", "laravel",
        "graphql", "rest api", "restful api", "grpc", "microservices"
    ],
    "AI / ML / Data Science": [
        "machine learning", "deep learning", "nlp", "natural language processing",
        "computer vision", "tensorflow", "pytorch", "keras", "scikit-learn",
        "sklearn", "pandas", "numpy", "opencv", "langchain", "langgraph", "rag",
        "retrieval augmented generation", "llm", "large language models", "bert",
        "transformers", "hugging face", "huggingface", "generative ai", "genai",
        "prompt engineering", "vector database", "pinecone", "faiss", "chromadb",
        "xgboost", "lightgbm", "mlops", "data science", "data analysis",
        "statistics", "a/b testing", "time series", "recommendation systems"
    ],
    "Data Engineering": [
        "pyspark", "spark", "apache spark", "kafka", "apache kafka", "airflow",
        "apache airflow", "etl", "elt", "hadoop", "hive", "databricks",
        "data pipeline", "data warehousing", "snowflake", "dbt", "big data"
    ],
    "Databases": [
        "mysql", "postgresql", "postgres", "mongodb", "sqlite", "redis",
        "cassandra", "oracle", "dynamodb", "elasticsearch", "firebase",
        "supabase", "mariadb", "neo4j"
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "azure", "gcp", "google cloud",
        "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins",
        "ci/cd", "github actions", "gitlab ci", "cloudformation", "linux",
        "nginx", "serverless", "lambda", "ec2", "s3"
    ],
    "Tools & Platforms": [
        "git", "github", "gitlab", "bitbucket", "jira", "confluence", "postman",
        "figma", "vs code", "visual studio", "swagger", "notion", "slack"
    ],
    "Testing": [
        "pytest", "unittest", "junit", "selenium", "cypress", "jest",
        "mocha", "test automation", "unit testing", "integration testing"
    ],
    "Soft Skills": [
        "leadership", "communication", "teamwork", "problem solving",
        "problem-solving", "critical thinking", "time management",
        "collaboration", "adaptability", "project management", "mentoring",
        "public speaking", "analytical skills", "attention to detail"
    ],
}

# Flat lookup: skill -> category, all lowercase for matching
SKILL_TO_CATEGORY = {
    skill.lower(): category
    for category, skills in SKILLS_DB.items()
    for skill in skills
}

DEGREE_KEYWORDS = [
    "b.tech", "btech", "bachelor of technology", "b.e.", "bachelor of engineering",
    "m.tech", "mtech", "master of technology", "b.sc", "bachelor of science",
    "m.sc", "master of science", "mba", "bba", "bca", "mca",
    "bachelor", "master", "phd", "ph.d", "doctorate", "diploma",
    "associate degree", "high school", "b.com", "m.com"
]

SECTION_HEADERS = {
    "education": ["education", "academic background", "academic qualifications", "qualifications"],
    "experience": ["experience", "work experience", "professional experience",
                   "employment history", "work history", "internship", "internships"],
    "skills": ["skills", "technical skills", "core competencies", "key skills",
               "skill set", "technologies", "tech stack"],
    "projects": ["projects", "personal projects", "academic projects", "key projects"],
    "certifications": ["certifications", "certificates", "licenses & certifications",
                        "courses", "certification"],
    "summary": ["summary", "objective", "professional summary", "career objective", "about me"],
    "achievements": ["achievements", "awards", "honors", "accomplishments"],
}
