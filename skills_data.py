"""
skills_data.py
The AI knowledge base of CareerAI.

Part 1 - SKILLS_DB      : curated catalog of ~100 skills with categories,
                          aliases/variants used by the NLP-style keyword
                          extraction engine (Modules 3, 4).
Part 2 - RESOURCES      : curated learning resources per skill used by the
                          Skill Gap Recommendation (Module 6) and the
                          Personalized Learning Path generator (Module 9).
"""

# ---------------------------------------------------------------------------
# PART 1 : SKILL CATALOG
#     skill_name : (category, [aliases ...])
# Aliases are matched with word-boundary style lookarounds, case-insensitive.
# ---------------------------------------------------------------------------
SKILLS_DB = {
    # ---------------- Programming Languages ----------------
    "Python":            ("Programming Languages", ["python3", "python 3"]),
    "Java":              ("Programming Languages", ["core java", "java 8", "java 11", "java 17"]),
    "C":                 ("Programming Languages", ["c language", "c programming"]),
    "C++":               ("Programming Languages", ["cpp", "c plus plus"]),
    "C#":                ("Programming Languages", ["csharp", "c sharp"]),
    "JavaScript":        ("Programming Languages", ["js", "es6", "ecmascript"]),
    "TypeScript":        ("Programming Languages", ["typescript 4", "typescript 5"]),
    "Golang":            ("Programming Languages", ["go language", "golang"]),
    "Rust":              ("Programming Languages", ["rust lang"]),
    "PHP":               ("Programming Languages", ["php 7", "php 8"]),
    "Ruby":              ("Programming Languages", ["ruby on rails"]),
    "Swift":             ("Programming Languages", ["swift 5"]),
    "Kotlin":            ("Programming Languages", ["kotlin android"]),
    "Scala":             ("Programming Languages", []),
    "R Programming":     ("Programming Languages", ["r language", "rstudio", "r studio", "r programming language"]),
    "MATLAB":            ("Programming Languages", ["mat lab"]),
    "Bash":              ("Programming Languages", ["shell scripting", "bash scripting", "bash shell"]),
    "Perl":              ("Programming Languages", []),
    "Dart":              ("Programming Languages", ["dart lang"]),

    # ---------------- Web Development ----------------
    "HTML":              ("Web Development", ["html5"]),
    "CSS":               ("Web Development", ["css3"]),
    "React":             ("Web Development", ["react.js", "reactjs", "react js", "react 18"]),
    "Angular":           ("Web Development", ["angularjs", "angular 2", "angular 12", "angular 16"]),
    "Vue.js":            ("Web Development", ["vue", "vuejs", "vue js"]),
    "Node.js":           ("Web Development", ["nodejs", "node js"]),
    "Express.js":        ("Web Development", ["expressjs", "express js", "express"]),
    "Django":            ("Web Development", ["django framework", "django rest framework", "drf"]),
    "Flask":             ("Web Development", ["flask framework", "flask restful"]),
    "Spring Boot":       ("Web Development", ["spring", "spring framework", "springboot", "spring mvc"]),
    "Laravel":           ("Web Development", []),
    "ASP.NET":           ("Web Development", [".net", "dotnet", "asp.net core", "asp net"]),
    "Next.js":           ("Web Development", ["nextjs", "next js"]),
    "Bootstrap":         ("Web Development", ["bootstrap 5", "bootstrap4"]),
    "Tailwind CSS":      ("Web Development", ["tailwind", "tailwindcss"]),
    "jQuery":            ("Web Development", ["jquery 3"]),
    "REST API":          ("Web Development", ["restful api", "rest apis", "restful services", "restful web services", "rest api development"]),
    "GraphQL":           ("Web Development", ["apollo graphql"]),
    "WordPress":         ("Web Development", ["wordpress cms", "woocommerce"]),

    # ---------------- Databases ----------------
    "SQL":                ("Databases", ["structured query language", "sql queries"]),
    "MySQL":              ("Databases", ["my sql", "mysql 8"]),
    "PostgreSQL":         ("Databases", ["postgres"]),
    "MongoDB":            ("Databases", ["mongo", "mongodb atlas"]),
    "Redis":              ("Databases", ["redis cache"]),
    "SQLite":             ("Databases", ["sqlite3"]),
    "Oracle DB":          ("Databases", ["oracle database", "oracle 11g", "oracle 12c", "pl/sql"]),
    "Microsoft SQL Server": ("Databases", ["sql server", "ms sql", "mssql", "t-sql"]),
    "Firebase":           ("Databases", ["google firebase", "firestore"]),
    "Database Management": ("Databases", ["dbms", "rdbms", "database design", "database systems"]),

    # ---------------- Data Science & Analytics ----------------
    "Data Analysis":      ("Data Science & Analytics", ["data analytics", "data insights", "analyzing data"]),
    "Data Visualization": ("Data Science & Analytics", ["data viz", "dashboards", "interactive dashboards"]),
    "Statistics":         ("Data Science & Analytics", ["statistical analysis", "statistical modeling", "probability", "hypothesis testing", "inferential statistics"]),
    "Pandas":             ("Data Science & Analytics", ["pandas library"]),
    "NumPy":              ("Data Science & Analytics", ["numpy arrays"]),
    "SciPy":              ("Data Science & Analytics", []),
    "Tableau":            ("Data Science & Analytics", ["tableau desktop", "tableau public"]),
    "Power BI":           ("Data Science & Analytics", ["powerbi", "power bi desktop", "dax"]),
    "Excel":              ("Data Science & Analytics", ["microsoft excel", "ms excel", "advanced excel", "excel macros", "vlookup"]),
    "Data Mining":        ("Data Science & Analytics", ["data extraction", "web scraping"]),
    "Big Data":           ("Data Science & Analytics", ["big data analytics", "bigdata"]),
    "Hadoop":             ("Data Science & Analytics", ["apache hadoop", "hive", "hdfs"]),
    "Spark":              ("Data Science & Analytics", ["apache spark", "pyspark"]),
    "ETL":                ("Data Science & Analytics", ["etl pipelines", "etl processes", "etl development"]),
    "Data Warehousing":   ("Data Science & Analytics", ["data warehouse", "dwh"]),
    "Snowflake":          ("Data Science & Analytics", []),

    # ---------------- AI & Machine Learning ----------------
    "Machine Learning":   ("AI & Machine Learning", ["ml", "ml algorithms", "supervised learning", "unsupervised learning"]),
    "Deep Learning":      ("AI & Machine Learning", ["deep neural networks", "neural networks", "cnn", "rnn", "lstm"]),
    "NLP":                ("AI & Machine Learning", ["natural language processing", "text mining", "text classification", "sentiment analysis"]),
    "Computer Vision":    ("AI & Machine Learning", ["image processing", "image classification", "object detection"]),
    "OpenCV":             ("AI & Machine Learning", []),
    "TensorFlow":         ("AI & Machine Learning", ["tf", "tensorflow 2"]),
    "PyTorch":            ("AI & Machine Learning", ["torch", "pytorch lightning"]),
    "Keras":              ("AI & Machine Learning", []),
    "Scikit-learn":       ("AI & Machine Learning", ["sklearn", "scikit learn", "scikit-learn"]),
    "Generative AI":      ("AI & Machine Learning", ["genai", "gen ai", "large language models", "llm", "llms", "chatgpt", "openai", "gpt", "gpt-4", "transformers"]),
    "Prompt Engineering": ("AI & Machine Learning", ["prompt design", "prompting"]),
    "Reinforcement Learning": ("AI & Machine Learning", ["q-learning", "deep rl"]),
    "MLOps":              ("AI & Machine Learning", ["ml ops", "model deployment", "model monitoring", "mlflow"]),
    "Artificial Intelligence": ("AI & Machine Learning", ["ai", "ai algorithms", "intelligent systems"]),

    # ---------------- Cloud & DevOps ----------------
    "AWS":                ("Cloud & DevOps", ["amazon web services", "ec2", "s3 bucket", "aws lambda", "aws cloud"]),
    "Azure":              ("Cloud & DevOps", ["microsoft azure", "azure devops"]),
    "Google Cloud":       ("Cloud & DevOps", ["gcp", "google cloud platform"]),
    "Docker":             ("Cloud & DevOps", ["containerization", "containers", "docker compose"]),
    "Kubernetes":         ("Cloud & DevOps", ["k8s", "kubectl"]),
    "Jenkins":            ("Cloud & DevOps", ["jenkins pipeline"]),
    "CI/CD":              ("Cloud & DevOps", ["cicd", "ci cd", "continuous integration", "continuous delivery", "continuous deployment", "github actions", "gitlab ci"]),
    "Git":                ("Cloud & DevOps", ["github", "gitlab", "bitbucket", "version control", "version control systems"]),
    "Linux":              ("Cloud & DevOps", ["unix", "linux administration", "ubuntu", "centos"]),
    "Terraform":          ("Cloud & DevOps", ["infrastructure as code", "iac"]),
    "Ansible":            ("Cloud & DevOps", ["ansible playbooks"]),
    "Microservices":      ("Cloud & DevOps", ["microservices architecture", "micro services", "micro-service"]),
    "Cloud Computing":    ("Cloud & DevOps", ["cloud platforms", "cloud services", "cloud native"]),
    "System Administration": ("Cloud & DevOps", ["server administration", "sysadmin"]),

    # ---------------- Mobile Development ----------------
    "Android":            ("Mobile Development", ["android development", "android sdk", "android studio", "android app"]),
    "iOS":                ("Mobile Development", ["ios development", "swiftui", "xcode"]),
    "Flutter":            ("Mobile Development", ["flutter sdk", "flutter app"]),
    "React Native":       ("Mobile Development", ["react-native", "react native app"]),
    "Mobile Development": ("Mobile Development", ["mobile app development", "mobile apps", "mobile application development"]),

    # ---------------- Software Engineering ----------------
    "OOP":                ("Software Engineering", ["object oriented programming", "object-oriented programming", "oops concepts", "oops"]),
    "Data Structures":    ("Software Engineering", ["dsa", "data structures and algorithms", "algorithms", "algorithm design"]),
    "System Design":      ("Software Engineering", ["system architecture", "software architecture", "high level design", "low level design", "hld", "lld"]),
    "Software Development": ("Software Engineering", ["software development life cycle", "sdlc", "software engineering"]),
    "Agile":              ("Software Engineering", ["scrum", "kanban", "agile methodology", "agile methodologies", "sprints"]),
    "Problem Solving":    ("Software Engineering", ["analytical thinking", "analytical skills", "logical thinking", "critical thinking"]),

    # ---------------- Testing & QA ----------------
    "Selenium":           ("Testing & QA", ["selenium webdriver", "selenium grid"]),
    "pytest":             ("Testing & QA", ["py.test", "pytest framework"]),
    "JUnit":              ("Testing & QA", ["junit 5"]),
    "Manual Testing":     ("Testing & QA", ["manual test cases", "manual testing of"]),
    "Automation Testing": ("Testing & QA", ["test automation", "automated testing", "automation frameworks"]),
    "Software Testing":   ("Testing & QA", ["qa testing", "quality assurance", "qa", "testing and debugging"]),
    "Postman":            ("Testing & QA", ["postman api", "postman collection"]),
    "API Testing":        ("Testing & QA", ["api test automation", "rest assured"]),
    "TestNG":             ("Testing & QA", ["test ng"]),

    # ---------------- Security ----------------
    "Network Security":   ("Security", ["information security", "infosec", "cyber security", "cybersecurity"]),
    "Ethical Hacking":    ("Security", ["penetration testing", "pen testing", "pentesting", "kali linux", "vulnerability scanning"]),
    "Cryptography":       ("Security", ["encryption", "encryption algorithms"]),
    "Firewalls":          ("Security", ["firewall", "ids", "ips", " intrusion detection"]),
    "SIEM":               ("Security", ["splunk", "qradar", "security information and event management"]),
    "Vulnerability Assessment": ("Security", ["vulnerability analysis", "vapt", "threat modeling"]),
    "Wireshark":          ("Security", ["packet analysis"]),

    # ---------------- Business & Soft Skills ----------------
    "Communication":      ("Business & Soft Skills", ["communication skills", "verbal communication", "written communication", "interpersonal skills"]),
    "Teamwork":           ("Business & Soft Skills", ["team collaboration", "collaboration", "team player", "cross-functional teams"]),
    "Leadership":         ("Business & Soft Skills", ["team leadership", "leading teams", "mentoring", "team management"]),
    "Project Management": ("Business & Soft Skills", ["project planning", "project coordination", "pmp", "ms project"]),
    "Business Analysis":  ("Business & Soft Skills", ["business analytics", "business requirements"]),
    "Requirements Gathering": ("Business & Soft Skills", ["requirements analysis", "requirement gathering", "brd", "functional specifications"]),
    "Stakeholder Management": ("Business & Soft Skills", ["stakeholder communication", "client interaction"]),
    "Presentation Skills": ("Business & Soft Skills", ["presentations", "presentation"]),
    "Time Management":    ("Business & Soft Skills", ["prioritization", "multitasking"]),
    "Digital Marketing":  ("Business & Soft Skills", ["seo", "sem", "social media marketing", "google analytics", "content marketing", "email marketing"]),
    "Technical Writing":  ("Business & Soft Skills", ["documentation", "technical documentation"]),
    "Customer Service":   ("Business & Soft Skills", ["client servicing", "customer support"]),
}

# Skills whose bare keyword is case-sensitive (single letters / risky matches)
CASE_SENSITIVE_SKILLS = {"C"}

# Related-skill knowledge: possessing the related skill gives partial credit
# for the target skill during gap analysis (Module 5).
RELATED_SKILLS = {
    "SQL": ["MySQL", "PostgreSQL", "Microsoft SQL Server", "SQLite", "Oracle DB"],
    "Machine Learning": ["Deep Learning", "Scikit-learn", "Statistics"],
    "Deep Learning": ["TensorFlow", "PyTorch", "Keras"],
    "Data Visualization": ["Tableau", "Power BI"],
    "OOP": ["Java", "Python", "C++", "C#"],
    "Data Analysis": ["Excel", "Pandas", "Statistics"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Mobile Development": ["Android", "iOS", "Flutter", "React Native"],
    "Software Testing": ["Manual Testing", "Automation Testing", "Selenium"],
    "Cloud Computing": ["AWS", "Azure", "Google Cloud"],
}

SKILL_CATEGORIES = [
    "Programming Languages",
    "Web Development",
    "Databases",
    "Data Science & Analytics",
    "AI & Machine Learning",
    "Cloud & DevOps",
    "Mobile Development",
    "Software Engineering",
    "Testing & QA",
    "Security",
    "Business & Soft Skills",
]

# Category -> Bootstrap badge color classes used across the UI
CATEGORY_COLORS = {
    "Programming Languages": "primary",
    "Web Development": "info",
    "Databases": "warning",
    "Data Science & Analytics": "success",
    "AI & Machine Learning": "danger",
    "Cloud & DevOps": "secondary",
    "Mobile Development": "purple",
    "Software Engineering": "teal",
    "Testing & QA": "orange",
    "Security": "dark",
    "Business & Soft Skills": "pink",
}


def category_of(skill_name, default="Other"):
    meta = SKILLS_DB.get(skill_name)
    return meta[0] if meta else default
