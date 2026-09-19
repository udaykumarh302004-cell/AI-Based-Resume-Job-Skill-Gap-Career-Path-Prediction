"""
career_data.py
Career knowledge base of CareerAI.

ROLE_PROFILES  : every known job role with weighted skill requirements
                 (weight 1 = nice to have ... 5 = must have). Used by
                 Module 8 (Job Role Recommendation), Module 5 (Gap
                 Analysis), Module 7 (Career Path Prediction) and
                 Module 9 (Learning Path).

CAREER_TRACKS  : ordered role ladders used by Module 7 to predict the
                 career progression path. `min_years` is the typical
                 lower bound of experience for that level.
"""

ROLE_PROFILES = {
    # ================= Software Development =================
    "Junior Software Developer": {
        "category": "Software Development",
        "description": "Entry-level developer writing and maintaining code under guidance.",
        "required_skills": {
            "Python": 3, "Java": 3, "C++": 2, "Data Structures": 4, "OOP": 4,
            "SQL": 2, "Git": 3, "Problem Solving": 3,
        },
        "typical_experience": "0-2 years",
        "min_years": 0.0,
    },
    "Software Engineer": {
        "category": "Software Development",
        "description": "Designs, builds and tests software features end to end.",
        "required_skills": {
            "Python": 3, "Java": 3, "Data Structures": 4, "OOP": 4, "SQL": 3,
            "Git": 4, "REST API": 3, "Agile": 3, "System Design": 2, "Problem Solving": 4,
        },
        "typical_experience": "2-5 years",
        "min_years": 1.5,
    },
    "Senior Software Engineer": {
        "category": "Software Development",
        "description": "Owns complex modules, reviews code and mentors junior developers.",
        "required_skills": {
            "System Design": 5, "OOP": 4, "Data Structures": 4, "Microservices": 3,
            "Docker": 3, "REST API": 4, "SQL": 3, "CI/CD": 3, "Leadership": 3, "Agile": 3,
        },
        "typical_experience": "5-8 years",
        "min_years": 4.0,
    },
    "Technical Lead": {
        "category": "Software Development",
        "description": "Leads the technical direction of a team and key projects.",
        "required_skills": {
            "System Design": 5, "Microservices": 4, "Docker": 3, "Kubernetes": 2,
            "CI/CD": 3, "Leadership": 5, "Communication": 4, "Agile": 4, "Code Review": 2,
        },
        "typical_experience": "8-12 years",
        "min_years": 7.0,
    },
    "Engineering Manager": {
        "category": "Software Development",
        "description": "Manages engineering teams, delivery and people growth.",
        "required_skills": {
            "Leadership": 5, "Project Management": 4, "Agile": 4, "Communication": 5,
            "System Design": 3, "Stakeholder Management": 4, "Teamwork": 4,
        },
        "typical_experience": "10+ years",
        "min_years": 9.0,
    },

    # ================= Web Development =================
    "Frontend Developer": {
        "category": "Web Development",
        "description": "Builds responsive, interactive user interfaces for web apps.",
        "required_skills": {
            "HTML": 5, "CSS": 5, "JavaScript": 5, "React": 4, "Bootstrap": 2,
            "REST API": 3, "Git": 3, "TypeScript": 2, "Tailwind CSS": 2,
        },
        "typical_experience": "0-4 years",
        "min_years": 0.0,
    },
    "Backend Developer": {
        "category": "Web Development",
        "description": "Builds server-side logic, APIs and database layers.",
        "required_skills": {
            "Python": 4, "Java": 3, "Node.js": 3, "SQL": 4, "REST API": 5,
            "Django": 3, "Flask": 3, "MongoDB": 2, "PostgreSQL": 3, "Docker": 2, "Git": 3,
        },
        "typical_experience": "0-5 years",
        "min_years": 0.0,
    },
    "Full Stack Developer": {
        "category": "Web Development",
        "description": "Develops both frontend and backend of web applications.",
        "required_skills": {
            "HTML": 4, "CSS": 4, "JavaScript": 5, "React": 4, "Node.js": 4,
            "SQL": 3, "MongoDB": 3, "REST API": 4, "Git": 3, "Express.js": 3,
        },
        "typical_experience": "1-5 years",
        "min_years": 0.5,
    },
    "Senior Full Stack Developer": {
        "category": "Web Development",
        "description": "Leads web application architecture and code quality.",
        "required_skills": {
            "JavaScript": 5, "React": 4, "Node.js": 4, "System Design": 4, "TypeScript": 3,
            "REST API": 4, "SQL": 3, "Docker": 3, "CI/CD": 3, "Leadership": 3,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },

    # ================= Data Science & AI =================
    "Data Analyst": {
        "category": "Data Science & AI",
        "description": "Turns raw data into reports, dashboards and business insights.",
        "required_skills": {
            "SQL": 5, "Excel": 5, "Power BI": 4, "Tableau": 3, "Python": 3,
            "Statistics": 3, "Data Visualization": 4, "Data Analysis": 5, "Communication": 3,
        },
        "typical_experience": "0-3 years",
        "min_years": 0.0,
    },
    "Data Scientist": {
        "category": "Data Science & AI",
        "description": "Builds predictive models and statistical solutions for business problems.",
        "required_skills": {
            "Python": 5, "Machine Learning": 5, "SQL": 4, "Statistics": 4,
            "Pandas": 4, "Data Visualization": 3, "Scikit-learn": 3, "Deep Learning": 2, "NLP": 2,
        },
        "typical_experience": "1-5 years",
        "min_years": 0.5,
    },
    "Senior Data Scientist": {
        "category": "Data Science & AI",
        "description": "Leads data science projects from framing to production deployment.",
        "required_skills": {
            "Machine Learning": 5, "Deep Learning": 4, "Python": 5, "Statistics": 5,
            "MLOps": 3, "NLP": 3, "Leadership": 3, "Data Storytelling": 2, "Spark": 2,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },
    "Machine Learning Engineer": {
        "category": "Data Science & AI",
        "description": "Productionizes ML models into scalable services and pipelines.",
        "required_skills": {
            "Python": 5, "Machine Learning": 5, "Deep Learning": 4, "TensorFlow": 3,
            "PyTorch": 3, "MLOps": 4, "Docker": 3, "SQL": 3, "Spark": 2, "AWS": 2,
        },
        "typical_experience": "2-6 years",
        "min_years": 1.0,
    },
    "AI Engineer": {
        "category": "Data Science & AI",
        "description": "Builds LLM / Generative-AI powered applications and agents.",
        "required_skills": {
            "Python": 5, "Generative AI": 5, "Machine Learning": 4, "Deep Learning": 4,
            "NLP": 4, "Prompt Engineering": 4, "TensorFlow": 2, "PyTorch": 3, "REST API": 3, "Docker": 2,
        },
        "typical_experience": "2-6 years",
        "min_years": 1.0,
    },

    # ================= Data Engineering =================
    "Data Engineer": {
        "category": "Data Engineering",
        "description": "Builds data pipelines, warehouses and big-data platforms.",
        "required_skills": {
            "Python": 4, "SQL": 5, "Spark": 4, "ETL": 5, "Hadoop": 3, "AWS": 3,
            "Data Warehousing": 4, "Big Data": 3, "Snowflake": 2, "Linux": 2,
        },
        "typical_experience": "1-5 years",
        "min_years": 0.5,
    },
    "Senior Data Engineer": {
        "category": "Data Engineering",
        "description": "Designs large-scale data architecture and mentors data engineers.",
        "required_skills": {
            "Spark": 5, "SQL": 5, "ETL": 5, "Data Warehousing": 4, "AWS": 4,
            "Kafka": 2, "System Design": 4, "Python": 4, "Leadership": 3,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },
    "Big Data Architect": {
        "category": "Data Engineering",
        "description": "Defines enterprise big-data strategy and reference architectures.",
        "required_skills": {
            "System Design": 5, "Big Data": 5, "Spark": 4, "Hadoop": 4, "Cloud Computing": 4,
            "Data Warehousing": 4, "Leadership": 4, "Communication": 4,
        },
        "typical_experience": "9+ years",
        "min_years": 8.0,
    },

    # ================= DevOps & Cloud =================
    "Cloud Engineer": {
        "category": "DevOps & Cloud",
        "description": "Deploys and manages cloud infrastructure and services.",
        "required_skills": {
            "AWS": 5, "Linux": 4, "Docker": 3, "Kubernetes": 3, "CI/CD": 3,
            "Terraform": 3, "Cloud Computing": 4, "Python": 2, "Git": 3,
        },
        "typical_experience": "1-5 years",
        "min_years": 0.5,
    },
    "DevOps Engineer": {
        "category": "DevOps & Cloud",
        "description": "Automates build, release and operations for software teams.",
        "required_skills": {
            "Linux": 5, "Docker": 5, "Kubernetes": 4, "CI/CD": 5, "Jenkins": 3,
            "AWS": 4, "Terraform": 3, "Ansible": 2, "Git": 4, "Python": 2,
        },
        "typical_experience": "2-6 years",
        "min_years": 1.0,
    },
    "Senior DevOps Engineer": {
        "category": "DevOps & Cloud",
        "description": "Owns platform reliability, observability and DevOps strategy.",
        "required_skills": {
            "Kubernetes": 5, "Docker": 4, "CI/CD": 5, "AWS": 4, "Terraform": 4,
            "System Design": 3, "Leadership": 3, "Linux": 4, "Microservices": 3,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },
    "Cloud Architect": {
        "category": "DevOps & Cloud",
        "description": "Designs enterprise cloud solutions, cost and security strategy.",
        "required_skills": {
            "System Design": 5, "AWS": 5, "Azure": 3, "Kubernetes": 4, "Terraform": 4,
            "Cloud Computing": 5, "Leadership": 4, "Communication": 4, "Microservices": 3,
        },
        "typical_experience": "9+ years",
        "min_years": 8.0,
    },

    # ================= Mobile Development =================
    "Junior Mobile Developer": {
        "category": "Mobile Development",
        "description": "Entry-level developer building simple mobile app screens and flows.",
        "required_skills": {
            "Java": 2, "Kotlin": 2, "Swift": 2, "Android": 3, "REST API": 2, "Git": 3, "OOP": 3,
        },
        "typical_experience": "0-2 years",
        "min_years": 0.0,
    },
    "Mobile App Developer": {
        "category": "Mobile Development",
        "description": "Develops complete cross-platform mobile applications.",
        "required_skills": {
            "Android": 4, "iOS": 3, "Flutter": 4, "React Native": 3, "Kotlin": 3,
            "Swift": 3, "REST API": 3, "Firebase": 3, "Git": 3, "OOP": 3,
        },
        "typical_experience": "1-5 years",
        "min_years": 0.5,
    },
    "Senior Mobile Developer": {
        "category": "Mobile Development",
        "description": "Architects mobile apps, performance and release pipelines.",
        "required_skills": {
            "Flutter": 4, "Android": 4, "iOS": 4, "System Design": 3, "CI/CD": 3,
            "REST API": 4, "Leadership": 3, "Firebase": 3, "Docker": 2,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },

    # ================= Testing & QA =================
    "QA Engineer": {
        "category": "Testing & QA",
        "description": "Designs and executes test plans for software quality.",
        "required_skills": {
            "Software Testing": 5, "Manual Testing": 4, "Automation Testing": 4,
            "Selenium": 3, "Java": 2, "Python": 2, "Postman": 3, "Agile": 3, "SQL": 2,
        },
        "typical_experience": "0-4 years",
        "min_years": 0.0,
    },
    "Senior QA Engineer": {
        "category": "Testing & QA",
        "description": "Owns test strategy, frameworks and quality gates.",
        "required_skills": {
            "Automation Testing": 5, "Selenium": 4, "Software Testing": 5, "API Testing": 4,
            "CI/CD": 3, "Python": 3, "Leadership": 3, "Agile": 4,
        },
        "typical_experience": "5-8 years",
        "min_years": 4.0,
    },

    # ================= Business =================
    "Business Analyst": {
        "category": "Business & Analytics",
        "description": "Bridges business needs and technical solutions with data-backed analysis.",
        "required_skills": {
            "Business Analysis": 5, "Requirements Gathering": 5, "Excel": 4, "SQL": 3,
            "Power BI": 3, "Communication": 4, "Agile": 3, "Stakeholder Management": 4,
        },
        "typical_experience": "0-4 years",
        "min_years": 0.0,
    },
    "Senior Business Analyst": {
        "category": "Business & Analytics",
        "description": "Leads requirement workshops and process improvement programs.",
        "required_skills": {
            "Business Analysis": 5, "Requirements Gathering": 5, "Stakeholder Management": 5,
            "SQL": 3, "Power BI": 3, "Leadership": 4, "Project Management": 4, "Communication": 5,
        },
        "typical_experience": "5-9 years",
        "min_years": 4.0,
    },

    # ================= Security =================
    "Cybersecurity Analyst": {
        "category": "Security",
        "description": "Monitors, detects and responds to security threats.",
        "required_skills": {
            "Network Security": 5, "Ethical Hacking": 4, "Cryptography": 3,
            "Firewalls": 3, "Linux": 3, "SIEM": 3, "Vulnerability Assessment": 4, "Problem Solving": 3,
        },
        "typical_experience": "0-5 years",
        "min_years": 0.0,
    },
    "Security Architect": {
        "category": "Security",
        "description": "Designs organization-wide security architecture and policy.",
        "required_skills": {
            "Network Security": 5, "System Design": 4, "Cryptography": 4, "SIEM": 3,
            "Cloud Computing": 3, "Leadership": 4, "Vulnerability Assessment": 4, "Communication": 4,
        },
        "typical_experience": "8+ years",
        "min_years": 7.0,
    },

    # ================= Digital Marketing =================
    "Digital Marketing Specialist": {
        "category": "Business & Analytics",
        "description": "Plans and runs online marketing campaigns and measures performance.",
        "required_skills": {
            "Digital Marketing": 5, "Excel": 3, "Data Analysis": 3,
            "Communication": 4, "Presentation Skills": 3, "Teamwork": 3,
        },
        "typical_experience": "0-4 years",
        "min_years": 0.0,
    },
}

# Skills that appear in ladders but are not standalone catalog skills get
# neutral treatment (no resources) - map them to a close real skill.
SKILL_ALIASES_FOR_PROFILES = {
    "Code Review": "Git",
    "Data Storytelling": "Data Visualization",
    "Kafka": "Big Data",
}


# ---------------------------------------------------------------------------
# CAREER TRACKS : ordered ladders (level 1 -> N) per domain
# ---------------------------------------------------------------------------
CAREER_TRACKS = [
    {
        "track": "Software Development",
        "icon": "bi-code-slash",
        "roles": [
            {"title": "Junior Software Developer", "level": 1, "years": "0-2"},
            {"title": "Software Engineer",         "level": 2, "years": "2-5"},
            {"title": "Senior Software Engineer",  "level": 3, "years": "5-8"},
            {"title": "Technical Lead",            "level": 4, "years": "8-12"},
            {"title": "Engineering Manager",       "level": 5, "years": "10+"},
        ],
    },
    {
        "track": "Web Development",
        "icon": "bi-window-sidebar",
        "roles": [
            {"title": "Frontend Developer",           "level": 1, "years": "0-2"},
            {"title": "Full Stack Developer",         "level": 2, "years": "1-5"},
            {"title": "Senior Full Stack Developer",  "level": 3, "years": "5-9"},
            {"title": "Technical Lead",               "level": 4, "years": "8-12"},
        ],
    },
    {
        "track": "Data Science & AI",
        "icon": "bi-graph-up-arrow",
        "roles": [
            {"title": "Data Analyst",            "level": 1, "years": "0-3"},
            {"title": "Data Scientist",          "level": 2, "years": "1-5"},
            {"title": "Senior Data Scientist",   "level": 3, "years": "5-9"},
            {"title": "AI Engineer",             "level": 4, "years": "2-6"},
        ],
    },
    {
        "track": "Data Engineering",
        "icon": "bi-database-gear",
        "roles": [
            {"title": "Data Analyst",           "level": 1, "years": "0-3"},
            {"title": "Data Engineer",          "level": 2, "years": "1-5"},
            {"title": "Senior Data Engineer",   "level": 3, "years": "5-9"},
            {"title": "Big Data Architect",     "level": 4, "years": "9+"},
        ],
    },
    {
        "track": "DevOps & Cloud",
        "icon": "bi-cloud-arrow-up",
        "roles": [
            {"title": "Cloud Engineer",          "level": 1, "years": "1-5"},
            {"title": "DevOps Engineer",         "level": 2, "years": "2-6"},
            {"title": "Senior DevOps Engineer",  "level": 3, "years": "5-9"},
            {"title": "Cloud Architect",         "level": 4, "years": "9+"},
        ],
    },
    {
        "track": "Mobile Development",
        "icon": "bi-phone",
        "roles": [
            {"title": "Junior Mobile Developer", "level": 1, "years": "0-2"},
            {"title": "Mobile App Developer",    "level": 2, "years": "1-5"},
            {"title": "Senior Mobile Developer", "level": 3, "years": "5-9"},
        ],
    },
    {
        "track": "Testing & QA",
        "icon": "bi-bug-check",
        "roles": [
            {"title": "QA Engineer",           "level": 1, "years": "0-4"},
            {"title": "Senior QA Engineer",    "level": 2, "years": "5-8"},
        ],
    },
    {
        "track": "Business & Analytics",
        "icon": "bi-briefcase",
        "roles": [
            {"title": "Business Analyst",           "level": 1, "years": "0-4"},
            {"title": "Senior Business Analyst",    "level": 2, "years": "5-9"},
            {"title": "Engineering Manager",        "level": 3, "years": "10+"},
        ],
    },
    {
        "track": "Cybersecurity",
        "icon": "bi-shield-lock",
        "roles": [
            {"title": "Cybersecurity Analyst", "level": 1, "years": "0-5"},
            {"title": "Security Architect",    "level": 2, "years": "8+"},
        ],
    },
]

# Title -> track lookup
TRACK_OF_ROLE = {
    r["title"]: t["track"] for t in CAREER_TRACKS for r in t["roles"]
}


def get_role_profile(title):
    return ROLE_PROFILES.get(title)


def get_required_skills(title):
    """Return weighted skill dict for a role (empty dict if unknown)."""
    profile = ROLE_PROFILES.get(title)
    return dict(profile["required_skills"]) if profile else {}
