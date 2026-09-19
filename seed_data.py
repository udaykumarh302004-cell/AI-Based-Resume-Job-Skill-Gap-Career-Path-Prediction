"""
seed_data.py
Sample job postings used by `python init_db.py` and the Admin
"Seed sample jobs" button (Module 12).
"""

SAMPLE_JOBS = [
    {
        "title": "Data Scientist",
        "company": "TechNova Analytics",
        "location": "Bengaluru, India",
        "job_type": "Full-time",
        "experience_level": "Mid-level",
        "category": "Data Science & AI",
        "salary_range": "12-18 LPA",
        "min_experience": 2.0,
        "skills_text": "Python, Machine Learning, SQL, Statistics, Pandas, Data Visualization, Tableau",
        "description": (
            "We are looking for a Data Scientist to join our analytics center of excellence. "
            "You will work with large datasets to build machine learning models that power "
            "business decisions. Requirements: strong hands-on experience with Python and "
            "libraries such as Pandas and NumPy; solid understanding of statistics and hypothesis "
            "testing; proficiency in SQL for data extraction; experience building machine learning "
            "models and evaluating them; data visualization skills using Tableau or Power BI. "
            "Candidates with 2+ years of experience and a bachelor's degree in a quantitative field "
            "are preferred. Full-time, hybrid role."
        ),
    },
    {
        "title": "Frontend Developer",
        "company": "WebCraft Studio",
        "location": "Remote (India)",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Web Development",
        "salary_range": "5-9 LPA",
        "min_experience": 0.0,
        "skills_text": "HTML, CSS, JavaScript, React, REST API, Git",
        "description": (
            "WebCraft Studio is hiring a Frontend Developer to build beautiful, responsive web "
            "applications for global clients. You should have expert knowledge of HTML5, CSS3 and "
            "modern JavaScript (ES6+). Experience with React is required, along with consuming "
            "REST APIs and working with Git version control. Familiarity with Bootstrap or Tailwind "
            "CSS is a plus. This is an entry level, full-time, remote friendly position - freshers "
            "with strong projects are encouraged to apply."
        ),
    },
    {
        "title": "Backend Developer (Python)",
        "company": "CloudSoft Systems",
        "location": "Hyderabad, India",
        "job_type": "Full-time",
        "experience_level": "Mid-level",
        "category": "Web Development",
        "salary_range": "8-14 LPA",
        "min_experience": 2.0,
        "skills_text": "Python, Django, REST API, PostgreSQL, Docker, AWS",
        "description": (
            "Join our backend engineering team to design scalable services used by millions. "
            "The ideal candidate has 2+ years of experience with Python, Django and RESTful API "
            "development. Strong SQL skills with PostgreSQL, understanding of database design, and "
            "hands-on Docker containerization are required. Exposure to AWS cloud deployment and "
            "CI/CD pipelines will be an advantage. You will collaborate in an Agile team with code "
            "reviews and Git based workflows."
        ),
    },
    {
        "title": "Full Stack Developer",
        "company": "StartUpX",
        "location": "Mumbai, India",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Web Development",
        "salary_range": "6-10 LPA",
        "min_experience": 1.0,
        "skills_text": "JavaScript, React, Node.js, MongoDB, Express.js, HTML, CSS",
        "description": (
            "StartUpX is building the next big fintech platform and needs a Full Stack Developer. "
            "You will own features end to end: crafting React interfaces on the frontend, building "
            "Node.js and Express.js APIs on the backend, and modeling data in MongoDB. "
            "Solid JavaScript fundamentals, HTML and CSS skills, REST API integration and Git "
            "workflow knowledge are expected. 1+ year of experience or strong open-source / project "
            "portfolio required. Energetic startup, full-time, hybrid."
        ),
    },
    {
        "title": "DevOps Engineer",
        "company": "InfraCloud Technologies",
        "location": "Pune, India",
        "job_type": "Full-time",
        "experience_level": "Mid-level",
        "category": "DevOps & Cloud",
        "salary_range": "10-16 LPA",
        "min_experience": 2.0,
        "skills_text": "Linux, Docker, Kubernetes, Jenkins, AWS, Terraform, CI/CD",
        "description": (
            "We are seeking a DevOps Engineer to automate our cloud platform. Core requirements: "
            "strong Linux administration, Docker containerization and Kubernetes orchestration. "
            "You will build CI/CD pipelines with Jenkins and GitHub Actions, provision infrastructure "
            "using Terraform, and manage workloads on AWS. Scripting knowledge in Python or Bash is "
            "expected. 2+ years of relevant experience in a full-time role. Agile environment with "
            "on-call rotation."
        ),
    },
    {
        "title": "Data Analyst",
        "company": "MarketRise Consulting",
        "location": "Delhi NCR, India",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Data Science & AI",
        "salary_range": "4-7 LPA",
        "min_experience": 0.0,
        "skills_text": "SQL, Excel, Power BI, Statistics, Data Visualization, Python",
        "description": (
            "MarketRise is hiring a Data Analyst to support our retail analytics practice. "
            "You will write advanced SQL queries, build interactive Power BI dashboards, and "
            "perform statistical analysis in Excel and Python. Requirements: strong SQL and Excel "
            "skills, data visualization expertise, basic statistics knowledge and excellent "
            "communication skills to present insights to stakeholders. Fresh graduates with 0-2 "
            "years of experience may apply. Full-time, on-site with hybrid flexibility."
        ),
    },
    {
        "title": "Machine Learning Engineer",
        "company": "AI Labs India",
        "location": "Bengaluru, India",
        "job_type": "Full-time",
        "experience_level": "Mid-level",
        "category": "Data Science & AI",
        "salary_range": "14-22 LPA",
        "min_experience": 2.0,
        "skills_text": "Python, TensorFlow, PyTorch, Deep Learning, MLOps, Docker, SQL",
        "description": (
            "AI Labs builds production machine learning systems for healthcare and fintech. "
            "We need a Machine Learning Engineer with strong Python, deep learning frameworks "
            "(TensorFlow and PyTorch), and experience deploying models using Docker and MLOps "
            "practices such as MLflow. Familiarity with NLP and computer vision projects, SQL data "
            "pipelines and AWS is a plus. 2+ years of experience building ML systems required. "
            "Full-time with flexible hours."
        ),
    },
    {
        "title": "Mobile App Developer (Flutter)",
        "company": "AppSphere Mobility",
        "location": "Chennai, India",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Mobile Development",
        "salary_range": "5-9 LPA",
        "min_experience": 1.0,
        "skills_text": "Flutter, Dart, Android, REST API, Firebase, Git",
        "description": (
            "AppSphere creates consumer apps with millions of downloads. We are hiring a Mobile App "
            "Developer with Flutter and Dart expertise to build cross-platform apps for Android and "
            "iOS. You will integrate REST APIs, use Firebase for authentication and push notifications, "
            "and follow Git based workflows. Knowledge of native Android development and OOP concepts "
            "is a plus. 1+ year of experience or strong Flutter portfolio required. Full-time, hybrid."
        ),
    },
    {
        "title": "Business Analyst",
        "company": "ConsultPro Advisors",
        "location": "Mumbai, India",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Business & Analytics",
        "salary_range": "5-8 LPA",
        "min_experience": 0.0,
        "skills_text": "Business Analysis, Requirements Gathering, Excel, SQL, Agile, Communication",
        "description": (
            "ConsultPro is looking for a Business Analyst to bridge business and technology teams. "
            "You will conduct requirements gathering workshops, prepare BRDs, analyze data in Excel "
            "and SQL, and support Agile delivery teams. Excellent communication and stakeholder "
            "management skills are essential. Exposure to Power BI dashboards is a plus. "
            "Bachelor's degree required; 0-2 years of experience. Full-time."
        ),
    },
    {
        "title": "Cybersecurity Analyst",
        "company": "SecureNet Solutions",
        "location": "Bengaluru, India",
        "job_type": "Full-time",
        "experience_level": "Entry level",
        "category": "Security",
        "salary_range": "6-10 LPA",
        "min_experience": 1.0,
        "skills_text": "Network Security, Ethical Hacking, Firewalls, SIEM, Linux, Cryptography",
        "description": (
            "SecureNet protects enterprises from evolving cyber threats. We need a Cybersecurity "
            "Analyst with knowledge of network security principles, firewalls and IDS/IPS, ethical "
            "hacking / penetration testing basics, and SIEM tools such as Splunk. Understanding of "
            "cryptography, Linux administration and vulnerability assessment (VAPT) is expected. "
            "Certifications like CEH or CompTIA Security+ are a plus. 1+ year of experience in a SOC "
            "or security team. Full-time, rotational shifts."
        ),
    },
]
