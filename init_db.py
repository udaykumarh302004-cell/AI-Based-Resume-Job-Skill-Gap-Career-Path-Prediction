"""
init_db.py
One-time database initialization & seeding.

    python init_db.py

Creates:
  - all database tables (careerai.db)
  - admin account     : admin@careerai.com / admin123
  - demo user account : demo@careerai.com  / demo123  (with a parsed sample resume)
  - 10 sample job postings (with AI-extracted required skills)
"""
import sys

from app import create_app
from extensions import db
from models import User, Resume, ExtractedSkill, Job, GapAnalysis, log_activity
from seed_data import SAMPLE_JOBS
from modules import resume_parser, skill_extractor
from modules.gap_analyzer import score_match
from routes.admin import _extract_job_skills

DEMO_RESUME_TEXT = """PRIYA SHARMA
Bengaluru, India | +91 98765 43210 | priya.sharma.demo@example.com
linkedin.com/in/priyasharma-demo

PROFESSIONAL SUMMARY
Final-year Computer Science student with 1 year of hands-on experience in data
analytics and machine learning projects, seeking a Data Analyst / Data Scientist role.

WORK EXPERIENCE
Data Analytics Intern, InfoEdge Solutions (Jun 2024 - Dec 2024)
- Analyzed 500K+ rows of sales data using Python, Pandas and NumPy
- Built interactive Power BI dashboards and automated weekly Excel reports
- Wrote advanced SQL queries for data extraction and transformation

SKILLS
Programming: Python, SQL, HTML, CSS, JavaScript
Data Science: Pandas, NumPy, Data Analysis, Data Visualization, Statistics,
Machine Learning (basic), Tableau, Power BI, Excel (advanced)
Tools: Git, GitHub, Jupyter Notebook

EDUCATION
B.E. Computer Science, Visvesvaraya Technological University (2022 - 2026)
CGPA: 8.7/10

PROJECTS
Customer Churn Prediction - built a machine learning model with Python and
Scikit-learn achieving 87% accuracy; performed statistical analysis and data
visualization with Matplotlib.

CERTIFICATIONS
Google Data Analytics Professional Certificate
"""

DEMO_RESUME_FILENAME = "priya_sharma_resume.txt"


def seed():
    app = create_app()
    with app.app_context():
        print("=" * 64)
        print("CareerAI - Database Initialization")
        print("=" * 64)

        db.create_all()
        print("[OK] Database tables created (careerai.db)")

        # ---------------- admin ----------------
        if not User.query.filter_by(email="admin@careerai.com").first():
            admin = User(name="System Administrator", email="admin@careerai.com", role="admin")
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
            print("[OK] Admin account created  ->  admin@careerai.com / admin123")
        else:
            print("[--] Admin account already exists")

        # ---------------- demo user ----------------
        demo = User.query.filter_by(email="demo@careerai.com").first()
        if not demo:
            demo = User(name="Priya Sharma (Demo)", email="demo@careerai.com", role="user")
            demo.set_password("demo123")
            db.session.add(demo)
            db.session.commit()
            print("[OK] Demo account created   ->  demo@careerai.com  / demo123")
        else:
            print("[--] Demo account already exists")

        # ---------------- demo resume + skills ----------------
        if not Resume.query.filter_by(user_id=demo.id).first():
            parsed = resume_parser.parse_resume_text(DEMO_RESUME_TEXT)
            resume = Resume(
                user_id=demo.id,
                original_filename=DEMO_RESUME_FILENAME,
                stored_filename=DEMO_RESUME_FILENAME,
                file_type="txt",
                raw_text=DEMO_RESUME_TEXT,
                candidate_name=parsed["candidate_name"],
                candidate_email=parsed["candidate_email"],
                candidate_phone=parsed["candidate_phone"],
                experience_years=parsed["experience_years"],
            )
            db.session.add(resume)
            db.session.flush()

            skills_dict, _ = skill_extractor.extract_skills_from_text(DEMO_RESUME_TEXT)
            for skill, info in skills_dict.items():
                db.session.add(ExtractedSkill(
                    resume_id=resume.id, skill_name=skill, category=info["category"],
                    frequency=info["frequency"], proficiency=info["proficiency"]))
            db.session.commit()
            print(f"[OK] Demo resume seeded with {len(skills_dict)} extracted skills")
        else:
            resume = Resume.query.filter_by(user_id=demo.id).first()
            print("[--] Demo resume already exists")

        # ---------------- sample jobs ----------------
        created_jobs = 0
        for jd in SAMPLE_JOBS:
            if Job.query.filter_by(title=jd["title"], company=jd["company"]).first():
                continue
            skills_json = _extract_job_skills({
                "title": jd["title"], "description": jd["description"],
                "skills_text": jd.get("skills_text", "")})
            db.session.add(Job(**jd, skills_json=skills_json))
            created_jobs += 1
        db.session.commit()
        print(f"[OK] Sample jobs created: {created_jobs} (total in DB: {Job.query.count()})")

        # ---------------- one demo gap analysis ----------------
        if not GapAnalysis.query.filter_by(user_id=demo.id).first():
            ds_job = Job.query.filter_by(title="Data Scientist").first()
            if ds_job and ds_job.skills_json:
                rows = ExtractedSkill.query.filter_by(resume_id=resume.id).all()
                user_skills = {r.skill_name: r.proficiency for r in rows}
                result = score_match(user_skills, ds_job.skills_json)
                db.session.add(GapAnalysis(
                    user_id=demo.id, job_id=ds_job.id, job_title=ds_job.title,
                    company=ds_job.company, match_percentage=result["match_percentage"],
                    verdict=result["verdict"],
                    matched_skills=result["matched"] + [dict(m) for m in result["matched_via"]],
                    missing_skills=result["missing"],
                    additional_skills=result["additional"][:15]))
                db.session.commit()
                print(f"[OK] Demo gap analysis created ({result['match_percentage']}% vs Data Scientist)")

        print("-" * 64)
        print("All done! Start the app with:  python app.py")
        print("Then open  http://127.0.0.1:5000")
        print("=" * 64)


if __name__ == "__main__":
    try:
        seed()
    except Exception as exc:
        print(f"[ERROR] Initialization failed: {exc}", file=sys.stderr)
        raise
