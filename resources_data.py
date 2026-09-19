"""
resources_data.py
Curated learning resources per skill (Module 6 - Skill Gap Recommendation,
Module 9 - Personalized Learning Path). For any skill not listed here a
smart fallback builds search links on popular learning platforms.
"""
from urllib.parse import quote_plus

# skill -> list of {course, platform, url, type, duration, level}
RESOURCES = {
    "Python": [
        {"course": "Python for Everybody Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python", "type": "Course", "duration": "8 weeks", "level": "Beginner"},
        {"course": "Python Full Course for Beginners", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "type": "Video", "duration": "4 hours", "level": "Beginner"},
        {"course": "Automate the Boring Stuff with Python", "platform": "Book (free online)", "url": "https://automatetheboringstuff.com/", "type": "Book", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Java": [
        {"course": "Java Programming and Software Engineering Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/java-programming", "type": "Course", "duration": "5 months", "level": "Beginner"},
        {"course": "Java Full Course", "platform": "YouTube (Bro Code)", "url": "https://www.youtube.com/watch?v=xk4_1vDrzzo", "type": "Video", "duration": "12 hours", "level": "Beginner"},
    ],
    "C++": [
        {"course": "C++ Tutorial for Beginners", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y", "type": "Video", "duration": "4 hours", "level": "Beginner"},
        {"course": "C++ Course - Learn C++ Programming", "platform": "Programiz", "url": "https://www.programiz.com/cpp-programming", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "JavaScript": [
        {"course": "The Modern JavaScript Tutorial", "platform": "javascript.info", "url": "https://javascript.info/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
        {"course": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "type": "Course", "duration": "300 hours", "level": "Beginner"},
    ],
    "HTML": [
        {"course": "Responsive Web Design Certification (HTML + CSS)", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "type": "Course", "duration": "300 hours", "level": "Beginner"},
        {"course": "Learn HTML", "platform": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "CSS": [
        {"course": "Learn CSS", "platform": "web.dev (Google)", "url": "https://web.dev/learn/css/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
        {"course": "CSS Tutorial", "platform": "W3Schools", "url": "https://www.w3schools.com/css/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "React": [
        {"course": "Learn React (official)", "platform": "react.dev", "url": "https://react.dev/learn", "type": "Docs", "duration": "Self-paced", "level": "Intermediate"},
        {"course": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "type": "Course", "duration": "48 hours", "level": "Intermediate"},
    ],
    "Node.js": [
        {"course": "Introduction to Node.js", "platform": "Node.js official", "url": "https://nodejs.org/en/learn", "type": "Docs", "duration": "Self-paced", "level": "Intermediate"},
        {"course": "Node.js and Express.js Full Course", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=Oe421Eje3GU", "type": "Video", "duration": "8 hours", "level": "Intermediate"},
    ],
    "SQL": [
        {"course": "SQL Tutorial", "platform": "W3Schools", "url": "https://www.w3schools.com/sql/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
        {"course": "Databases and SQL for Data Science", "platform": "Coursera (IBM)", "url": "https://www.coursera.org/learn/sql-data-science", "type": "Course", "duration": "4 weeks", "level": "Beginner"},
        {"course": "SQLBolt - Interactive SQL Lessons", "platform": "SQLBolt", "url": "https://sqlbolt.com/", "type": "Interactive", "duration": "Self-paced", "level": "Beginner"},
    ],
    "MySQL": [
        {"course": "MySQL Tutorial", "platform": "W3Schools", "url": "https://www.w3schools.com/mysql/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
        {"course": "SQL - MySQL for Data Analytics and Business Intelligence", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "PostgreSQL": [
        {"course": "PostgreSQL Tutorial", "platform": "postgresqltutorial.com", "url": "https://www.postgresqltutorial.com/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "MongoDB": [
        {"course": "MongoDB University Free Courses", "platform": "MongoDB", "url": "https://learn.mongodb.com/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Machine Learning": [
        {"course": "Machine Learning Specialization (Andrew Ng)", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning-introduction", "type": "Course", "duration": "3 months", "level": "Intermediate"},
        {"course": "Intro to Machine Learning", "platform": "Kaggle Learn", "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "type": "Course", "duration": "3 hours", "level": "Beginner"},
    ],
    "Deep Learning": [
        {"course": "Deep Learning Specialization", "platform": "Coursera (DeepLearning.AI)", "url": "https://www.coursera.org/specializations/deep-learning", "type": "Course", "duration": "4 months", "level": "Advanced"},
        {"course": "Practical Deep Learning for Coders", "platform": "fast.ai", "url": "https://course.fast.ai/", "type": "Course", "duration": "10 weeks", "level": "Intermediate"},
    ],
    "Statistics": [
        {"course": "Statistics and Probability", "platform": "Khan Academy", "url": "https://www.khanacademy.org/math/statistics-probability", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Data Analysis": [
        {"course": "Data Analysis with Python", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/", "type": "Course", "duration": "300 hours", "level": "Beginner"},
        {"course": "Google Data Analytics Professional Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-data-analytics", "type": "Course", "duration": "6 months", "level": "Beginner"},
    ],
    "Data Visualization": [
        {"course": "Data Visualization", "platform": "Kaggle Learn", "url": "https://www.kaggle.com/learn/data-visualization", "type": "Course", "duration": "4 hours", "level": "Beginner"},
    ],
    "Pandas": [
        {"course": "Pandas Documentation - 10 Minutes to pandas", "platform": "pandas.pydata.org", "url": "https://pandas.pydata.org/docs/user_guide/10min.html", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
        {"course": "Data Analysis with Python Course (Pandas + NumPy)", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=r-uOLxNrNk8", "type": "Video", "duration": "10 hours", "level": "Beginner"},
    ],
    "NumPy": [
        {"course": "NumPy Quickstart", "platform": "numpy.org", "url": "https://numpy.org/doc/stable/user/quickstart.html", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Tableau": [
        {"course": "Tableau Free Training Videos", "platform": "Tableau", "url": "https://www.tableau.com/learn/training", "type": "Video", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Power BI": [
        {"course": "Get started with Microsoft Power BI", "platform": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/training/paths/create-analyze-data-with-power-bi/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Excel": [
        {"course": "Excel Skills for Business Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/excel", "type": "Course", "duration": "4 months", "level": "Beginner"},
    ],
    "AWS": [
        {"course": "AWS Cloud Quest / AWS Skill Builder", "platform": "AWS (official)", "url": "https://skillbuilder.aws/", "type": "Interactive", "duration": "Self-paced", "level": "Beginner"},
        {"course": "AWS Fundamentals Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/aws-fundamentals", "type": "Course", "duration": "4 months", "level": "Beginner"},
    ],
    "Azure": [
        {"course": "Microsoft Azure Fundamentals (AZ-900) Learning Path", "platform": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Google Cloud": [
        {"course": "Google Cloud Skills Boost", "platform": "Google Cloud", "url": "https://www.cloudskillsboost.google/", "type": "Interactive", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Docker": [
        {"course": "Docker Get Started (official)", "platform": "Docker Docs", "url": "https://docs.docker.com/get-started/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
        {"course": "Docker Tutorial for Beginners", "platform": "YouTube (TechWorld with Nana)", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE", "type": "Video", "duration": "3 hours", "level": "Beginner"},
    ],
    "Kubernetes": [
        {"course": "Kubernetes Basics (official tutorials)", "platform": "kubernetes.io", "url": "https://kubernetes.io/docs/tutorials/", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Jenkins": [
        {"course": "Jenkins Tutorial (official)", "platform": "jenkins.io", "url": "https://www.jenkins.io/doc/tutorials/", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "CI/CD": [
        {"course": "GitHub Actions - Learn", "platform": "GitHub", "url": "https://github.com/features/actions", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Git": [
        {"course": "Pro Git (free book)", "platform": "git-scm.com", "url": "https://git-scm.com/book/en/v2", "type": "Book", "duration": "Self-paced", "level": "Beginner"},
        {"course": "Learn Git Branching (interactive)", "platform": "learngitbranching.js.org", "url": "https://learngitbranching.js.org/", "type": "Interactive", "duration": "3 hours", "level": "Beginner"},
    ],
    "Linux": [
        {"course": "Linux Journey (free course)", "platform": "linuxjourney.com", "url": "https://linuxjourney.com/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Terraform": [
        {"course": "Terraform Tutorials (official)", "platform": "HashiCorp", "url": "https://developer.hashicorp.com/terraform/tutorials", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "TensorFlow": [
        {"course": "TensorFlow Official Tutorials", "platform": "tensorflow.org", "url": "https://www.tensorflow.org/tutorials", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "PyTorch": [
        {"course": "PyTorch Official Tutorials", "platform": "pytorch.org", "url": "https://pytorch.org/tutorials/", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Scikit-learn": [
        {"course": "Scikit-learn Getting Started Guide", "platform": "scikit-learn.org", "url": "https://scikit-learn.org/stable/getting_started.html", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "NLP": [
        {"course": "Hugging Face NLP Course", "platform": "Hugging Face", "url": "https://huggingface.co/learn/nlp-course", "type": "Course", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Generative AI": [
        {"course": "Short Courses on LLMs & GenAI", "platform": "DeepLearning.AI", "url": "https://www.deeplearning.ai/short-courses/", "type": "Course", "duration": "1-2 hours each", "level": "Intermediate"},
        {"course": "Generative AI for Everyone", "platform": "Coursera (DeepLearning.AI)", "url": "https://www.coursera.org/learn/generative-ai-for-everyone", "type": "Course", "duration": "5 hours", "level": "Beginner"},
    ],
    "Prompt Engineering": [
        {"course": "Prompt Engineering Guide", "platform": "promptingguide.ai", "url": "https://www.promptingguide.ai/", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Spark": [
        {"course": "Apache Spark Quick Start (official)", "platform": "spark.apache.org", "url": "https://spark.apache.org/docs/latest/quick-start.html", "type": "Tutorial", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Hadoop": [
        {"course": "Hadoop Tutorial", "platform": "Guru99", "url": "https://www.guru99.com/hadoop-tutorial.html", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "ETL": [
        {"course": "ETL Pipelines with Python", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=etl+pipeline+python+tutorial", "type": "Video", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Django": [
        {"course": "Django Official Tutorial (Polls App)", "platform": "djangoproject.com", "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Flask": [
        {"course": "Flask Official Tutorial", "platform": "flask.palletsprojects.com", "url": "https://flask.palletsprojects.com/tutorial/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Spring Boot": [
        {"course": "Spring Boot - Building an Application (official guide)", "platform": "spring.io", "url": "https://spring.io/guides/gs/spring-boot", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "REST API": [
        {"course": "REST API Tutorial (concepts)", "platform": "restfulapi.net", "url": "https://restfulapi.net/", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Android": [
        {"course": "Android Basics with Compose (official)", "platform": "Google Developers Training", "url": "https://developer.android.com/courses/android-basics-compose/course", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "iOS": [
        {"course": "Develop in Swift Tutorials (official)", "platform": "Apple Developer", "url": "https://developer.apple.com/tutorials/develop-in-swift", "type": "Tutorial", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Flutter": [
        {"course": "Flutter Codelabs (official)", "platform": "Google Flutter", "url": "https://codelabs.developers.google.com/?product=flutter", "type": "Interactive", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Selenium": [
        {"course": "Selenium with Python (official docs)", "platform": "selenium.dev", "url": "https://www.selenium.dev/documentation/webdriver/", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Software Testing": [
        {"course": "Software Testing Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/software-testing", "type": "Course", "duration": "4 months", "level": "Beginner"},
    ],
    "Network Security": [
        {"course": "Introduction to Cyber Security Specialization", "platform": "Coursera (NYU)", "url": "https://www.coursera.org/specializations/intro-cyber-security", "type": "Course", "duration": "4 months", "level": "Beginner"},
    ],
    "Ethical Hacking": [
        {"course": "Complete Ethical Hacking Course", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=w8aKFNvJd4k", "type": "Video", "duration": "13 hours", "level": "Beginner"},
    ],
    "Cryptography": [
        {"course": "Cryptography I", "platform": "Coursera (Stanford)", "url": "https://www.coursera.org/learn/crypto", "type": "Course", "duration": "6 weeks", "level": "Intermediate"},
    ],
    "Business Analysis": [
        {"course": "Business Analysis Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/topic/business-analysis/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Communication": [
        {"course": "Improving Communication Skills", "platform": "Coursera (Wharton)", "url": "https://www.coursera.org/learn/wharton-communication-skills", "type": "Course", "duration": "4 weeks", "level": "Beginner"},
    ],
    "Project Management": [
        {"course": "Google Project Management Professional Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-project-management", "type": "Course", "duration": "6 months", "level": "Beginner"},
    ],
    "Agile": [
        {"course": "Agile with Atlassian Jira", "platform": "Coursera", "url": "https://www.coursera.org/learn/agile-atlassian-jira", "type": "Course", "duration": "4 weeks", "level": "Beginner"},
    ],
    "OOP": [
        {"course": "Object-Oriented Programming Basics", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=object+oriented+programming+course", "type": "Video", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Data Structures": [
        {"course": "Algorithms Specialization", "platform": "Coursera (Stanford)", "url": "https://www.coursera.org/specializations/algorithms", "type": "Course", "duration": "4 months", "level": "Intermediate"},
        {"course": "Data Structures Easy to Advanced Course", "platform": "YouTube (freeCodeCamp)", "url": "https://www.youtube.com/watch?v=RBSGKlAovoE", "type": "Video", "duration": "8 hours", "level": "Beginner"},
    ],
    "System Design": [
        {"course": "System Design Primer (GitHub)", "platform": "GitHub", "url": "https://github.com/donnemartin/system-design-primer", "type": "Docs", "duration": "Self-paced", "level": "Advanced"},
    ],
    "Digital Marketing": [
        {"course": "Fundamentals of Digital Marketing", "platform": "Google Digital Garage", "url": "https://learndigital.withgoogle.com/digitalgarage/course/digital-marketing", "type": "Course", "duration": "40 hours", "level": "Beginner"},
    ],
    "Leadership": [
        {"course": "Leading Teams", "platform": "Coursera (Michigan)", "url": "https://www.coursera.org/learn/leading-teams", "type": "Course", "duration": "4 weeks", "level": "Beginner"},
    ],
    "MLOps": [
        {"course": "MLOps Specialization", "platform": "Coursera (DeepLearning.AI)", "url": "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops", "type": "Course", "duration": "4 months", "level": "Advanced"},
    ],
    "TypeScript": [
        {"course": "TypeScript Handbook (official)", "platform": "typescriptlang.org", "url": "https://www.typescriptlang.org/docs/handbook/intro.html", "type": "Docs", "duration": "Self-paced", "level": "Intermediate"},
    ],
    "Kotlin": [
        {"course": "Kotlin Basics (JetBrains Academy)", "platform": "JetBrains", "url": "https://www.jetbrains.com/academy/", "type": "Course", "duration": "Self-paced", "level": "Beginner"},
    ],
    "Swift": [
        {"course": "Swift Programming Language Guide (official)", "platform": "Apple", "url": "https://docs.swift.org/swift-book/", "type": "Docs", "duration": "Self-paced", "level": "Beginner"},
    ],
}

PLATFORM_ICONS = {
    "Coursera": "bi-mortarboard",
    "Udemy": "bi-play-btn",
    "YouTube": "bi-youtube",
    "YouTube (freeCodeCamp)": "bi-youtube",
    "YouTube (Bro Code)": "bi-youtube",
    "YouTube (TechWorld with Nana)": "bi-youtube",
    "freeCodeCamp": "bi-fire",
    "Kaggle Learn": "bi-bar-chart",
    "Microsoft Learn": "bi-microsoft",
    "MDN Web Docs": "bi-file-code",
    "Docs": "bi-book",
}


def get_resources(skill_name):
    """Return curated resources for a skill, or smart fallback search links."""
    if skill_name in RESOURCES:
        return RESOURCES[skill_name]
    q = quote_plus(skill_name)
    return [
        {"course": f"{skill_name} - courses & specializations", "platform": "Coursera",
         "url": f"https://www.coursera.org/search?query={q}", "type": "Course",
         "duration": "Self-paced", "level": "Beginner"},
        {"course": f"{skill_name} - top rated courses", "platform": "Udemy",
         "url": f"https://www.udemy.com/courses/search/?q={q}", "type": "Course",
         "duration": "Self-paced", "level": "All levels"},
        {"course": f"{skill_name} - free video tutorials", "platform": "YouTube",
         "url": f"https://www.youtube.com/results?search_query={q}+tutorial", "type": "Video",
         "duration": "Free", "level": "All levels"},
    ]
