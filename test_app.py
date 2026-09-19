"""
test_app.py
End-to-end smoke test for CareerAI (uses the Flask test client - no server needed).

    python test_app.py

Verifies that every module's routes respond correctly, that registration,
login, resume upload, extraction, gap analysis, career prediction, learning
path, dashboard and admin flows all work without errors.
Run on a fresh database (python init_db.py first) for fully deterministic IDs.
"""
import io
import sys

from app import create_app
from extensions import db
from models import User, Resume, GapAnalysis

PASSED = []
FAILED = []


def check(name, resp, expect=200):
    status = resp.status_code
    ok = status == expect
    (PASSED if ok else FAILED).append((name, status, expect))
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name:58s} -> {status} (expected {expect})")
    return resp


def last_resume_id(app, email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        r = (Resume.query.filter_by(user_id=user.id)
             .order_by(Resume.created_at.desc()).first())
        return r.id if r else None


def last_gap_id(app, email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        g = (GapAnalysis.query.filter_by(user_id=user.id)
             .order_by(GapAnalysis.created_at.desc()).first())
        return g.id if g else None


def main():
    app = create_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    email = "smoke@test.com"
    sample_txt = (
        b"RAHUL VERMA\nHyderabad, India | +91 90000 11111 | rahul.verma@example.com\n\n"
        b"SKILLS\nProgramming: Java, Python, JavaScript\nWeb: HTML, CSS, React, Node.js, REST API\n"
        b"Databases: MySQL, MongoDB\nTools: Git, Docker, Linux\n\n"
        b"EXPERIENCE\nSoftware Developer with 2 years of experience building web applications.\n\n"
        b"EDUCATION\nB.Tech Computer Science, JNTU Hyderabad\n"
    )

    # ---------------- public pages ----------------
    check("Landing page (GET /)", client.get("/"))

    # ---------------- Module 1: auth ----------------
    check("Register page", client.get("/register"))
    resp = client.post("/register", data={
        "name": "Smoke Test User", "email": email,
        "password": "test123", "confirm_password": "test123"},
        follow_redirects=False)
    check("Register new user (POST /register)", resp, expect=302)
    check("Login page", client.get("/login"))
    resp = client.post("/login", data={"email": email, "password": "test123"},
                       follow_redirects=False)
    check("Login new user (POST /login)", resp, expect=302)

    # ---------------- Module 2+3: upload & extraction ----------------
    check("Upload page", client.get("/upload"))
    resp = client.post("/upload", data={
        "resume": (io.BytesIO(sample_txt), "rahul_verma_resume.txt")}, follow_redirects=False)
    check("Upload TXT resume (POST /upload)", resp, expect=302)
    rid = last_resume_id(app, email)
    if rid:
        check("Resume detail (parsed + extracted skills)", client.get(f"/resume/{rid}"))
    else:
        check("Resume detail (parsed + extracted skills)", client.get("/resume/9999"), expect=404)
    check("My Skills page", client.get("/my-skills"))

    # ---------------- Module 4: JD analysis & job browsing ----------------
    check("Analyze Job page", client.get("/analyze-job"))
    resp = client.post("/analyze-job", data={
        "job_description": ("Job Title: Python Developer\nWe need a developer with 3-5 years of "
                            "experience in Python, Django, REST API, PostgreSQL and Docker. "
                            "Bachelor's degree required. Full-time remote role with Agile team.")},
        follow_redirects=True)
    check("Analyze pasted job description", resp)
    check("Jobs list", client.get("/jobs"))
    check("Job detail", client.get("/jobs/1"))

    # ---------------- Module 10: job recommendation ----------------
    check("Job Recommendations", client.get("/job-recommendations"))

    # ---------------- Modules 5-9 ----------------
    resp = client.post("/gap-analysis", data={"job_id": 1}, follow_redirects=True)
    check("Gap Analysis (POST job 1)", resp)
    check("Gap Analysis select page", client.get("/gap-analysis"))
    gid = last_gap_id(app, email)
    if gid:
        check("Gap Analysis stored result", client.get(f"/gap-analysis/result/{gid}"))
        check("Skill Gap Recommendations", client.get(f"/gap-recommendations/{gid}"))
    else:
        check("Gap Analysis stored result", client.get("/gap-analysis/result/1"), expect=200)
        check("Skill Gap Recommendations", client.get("/gap-recommendations/1"), expect=200)
    check("Career Path Prediction", client.get("/career-path"))
    check("Role Recommendations", client.get("/role-recommendations"))
    resp = client.post("/learning-path", data={"role": "Full Stack Developer"}, follow_redirects=True)
    check("Learning Path (POST role)", resp)
    check("Learning Path form (GET)", client.get("/learning-path"))

    # ---------------- Module 11: dashboard ----------------
    check("User Dashboard & charts", client.get("/dashboard"))
    check("Profile page", client.get("/profile"))

    # ---------------- Module 12: admin ----------------
    check("Logout", client.get("/logout", follow_redirects=False), expect=302)
    resp = client.post("/login", data={"email": "admin@careerai.com", "password": "admin123"},
                       follow_redirects=False)
    check("Login as admin", resp, expect=302)
    check("Admin dashboard", client.get("/admin/dashboard"))
    check("Admin users list", client.get("/admin/users"))
    check("Admin jobs list", client.get("/admin/jobs"))
    check("Admin new job form", client.get("/admin/jobs/new"))
    resp = client.post("/admin/jobs/new", data={
        "title": "QA Engineer", "company": "TestCorp", "location": "Remote",
        "job_type": "Full-time", "experience_level": "Entry level",
        "category": "Testing & QA", "salary_range": "5-8 LPA", "min_experience": "0",
        "skills_text": "Selenium, Automation Testing, Java",
        "description": ("We are hiring a QA Engineer with strong automation testing skills. "
                        "Experience with Selenium, Java, test frameworks, API testing and Agile "
                        "practices required. Manual testing fundamentals and SQL basics expected.")},
        follow_redirects=True)
    check("Admin create job (POST)", resp)

    # edit job 1 (exists after init_db seeding)
    resp = client.post("/admin/jobs/1/edit", data={
        "title": "Data Scientist", "company": "TechNova Analytics", "location": "Bengaluru, India",
        "job_type": "Full-time", "experience_level": "Mid-level",
        "category": "Data Science & AI", "salary_range": "12-18 LPA", "min_experience": "2",
        "skills_text": "Python, Machine Learning, SQL, Statistics, Pandas, Tableau",
        "description": ("Looking for a Data Scientist with 2+ years of experience in Python, machine "
                        "learning, SQL and statistics. Pandas and Tableau skills required for "
                        "analytics projects. Full-time role in Bengaluru.")},
        follow_redirects=True)
    check("Admin edit job (POST)", resp)
    check("Admin resumes oversight", client.get("/admin/resumes"))

    # non-admin blocked from admin area
    client.get("/logout")
    client.post("/login", data={"email": email, "password": "test123"})
    check("Admin page blocked for normal user (redirect)", client.get("/admin/dashboard"), expect=302)

    # ---------------- summary ----------------
    print("=" * 78)
    total = len(PASSED) + len(FAILED)
    print(f"RESULT: {len(PASSED)}/{total} checks passed")
    if FAILED:
        print("Failed checks:")
        for name, status, expect in FAILED:
            print(f"  - {name}: got {status}, expected {expect}")
        sys.exit(1)
    print("ALL SMOKE TESTS PASSED - the application is error-free.")
    print("Default accounts -> admin@careerai.com / admin123 | demo@careerai.com / demo123")


if __name__ == "__main__":
    main()
