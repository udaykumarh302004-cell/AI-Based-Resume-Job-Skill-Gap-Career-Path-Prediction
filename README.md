# CareerAI - AI-Based Resume–Job Skill Gap & Career Path Prediction System

A complete **Python Flask** web application that analyzes resumes against job
requirements using an AI keyword-matching engine, identifies skill gaps,
recommends what to learn, and predicts career progression paths.

---

## 1. The 12 Modules

| # | Module | Where to find it |
|---|--------|------------------|
| 1 | User Registration & Login | `/register`, `/login`, `/logout`, `/profile` |
| 2 | Resume Upload & Parsing | `/upload` (PDF / DOCX / TXT) |
| 3 | Resume Skill Extraction | Automatic after upload - shown on `/resume/<id>` and `/my-skills` |
| 4 | Job Description Analysis | `/analyze-job` (paste any JD) + admin job postings |
| 5 | Skill Matching & Gap Analysis | `/gap-analysis` |
| 6 | Skill Gap Recommendation | `/gap-recommendations/<id>` |
| 7 | Career Path Prediction | `/career-path` |
| 8 | Job Role Recommendation | `/role-recommendations` |
| 9 | Personalized Learning Path | `/learning-path` |
| 10 | Job Recommendation | `/job-recommendations` |
| 11 | Dashboard & Visualization | `/dashboard` (4 interactive Chart.js charts) |
| 12 | Admin Module | `/admin/dashboard` (users, jobs CRUD, resumes, analytics) |

## 2. Technology Stack

- **Backend:** Python 3.9+ / Flask 3, Flask-SQLAlchemy, Flask-Login, Werkzeug
- **Database:** SQLite (file `careerai.db` - zero configuration)
- **Resume parsing:** PyPDF2 (PDF), python-docx (DOCX), built-in TXT reader
- **AI engine:** weighted skill knowledge base (100+ skills, 25+ roles,
  9 career tracks) with word-boundary NLP keyword matching, proficiency
  estimation, weighted gap scoring and related-skill partial credit
- **Frontend:** Bootstrap 5, Bootstrap Icons, Chart.js (CDN), custom CSS

## 3. Quick Start

### Option A - one-click scripts
- **Windows:** double-click `run.bat`
- **Linux / macOS:** `bash run.sh`

### Option B - manual steps

```bash
# 1) create a virtual environment (recommended)
python -m venv venv

# activate it
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS

# 2) install dependencies
pip install -r requirements.txt

# 3) initialize the database (creates tables + demo data)
python init_db.py

# 4) run the app
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

### Optional - verify everything works

```bash
python test_app.py
```

Runs ~30 end-to-end checks against every module using the Flask test client.

## 4. Default Accounts (created by `init_db.py`)

| Role  | Email                | Password  |
|-------|----------------------|-----------|
| Admin | admin@careerai.com   | admin123  |
| Demo user | demo@careerai.com | demo123  |

The demo user already has a parsed resume with extracted skills and one gap
analysis, so the dashboard and charts work immediately. 10 sample job
postings are also seeded.

## 5. Project Structure

```
AI_Resume_Career_Predictor/
├── app.py                  # Flask app factory & entry point
├── config.py               # Configuration (DB, uploads, secrets)
├── extensions.py           # SQLAlchemy / Flask-Login instances
├── models.py               # Database models (User, Resume, Job, ...)
├── skills_data.py          # Knowledge base: 100+ skills + aliases
├── career_data.py          # Knowledge base: 25+ roles, 9 career tracks
├── resources_data.py       # Learning resources + smart fallback links
├── seed_data.py            # 10 sample job postings
├── init_db.py              # DB creation & seeding (run once)
├── test_app.py             # End-to-end smoke tests
├── run.bat / run.sh        # One-click launchers
├── requirements.txt
├── modules/                # Core AI engine (Modules 2-10 logic)
│   ├── resume_parser.py    #   Module 2: text extraction & field parsing
│   ├── skill_extractor.py  #   Module 3: NLP skill extraction
│   ├── job_analyzer.py     #   Module 4: JD analysis
│   ├── gap_analyzer.py     #   Modules 5+6: weighted matching & recommendations
│   ├── career_predictor.py #   Module 7: career path prediction
│   ├── role_recommender.py #   Module 8: role recommendation
│   ├── learning_path.py    #   Module 9: phased learning roadmap
│   └── job_recommender.py  #   Module 10: job ranking
├── routes/                 # Flask blueprints (web layer)
│   ├── main.py             #   Landing page
│   ├── auth.py             #   Module 1
│   ├── resume.py           #   Modules 2+3
│   ├── jobs.py             #   Module 4 + 10 + job browsing
│   ├── analysis.py         #   Modules 5-9
│   ├── dashboard.py        #   Module 11
│   └── admin.py            #   Module 12
├── templates/              # Jinja2 HTML templates (Bootstrap 5)
├── static/                 # CSS + JS
├── sample_data/            # Sample resumes for testing uploads
└── uploads/                # Uploaded resume storage (auto-created)
```

## 6. How the AI Matching Works

1. **Extraction (Modules 3-4):** the resume/JD text is scanned against a
   curated skill catalog using word-boundary regex (aliases included, e.g.
   `reactjs -> React`). Proficiency is estimated from mention frequency and
   qualifier words ("advanced", "basic"...).
2. **Weighted gap scoring (Module 5):** every job skill has an importance
   weight (1-5). The match % is the weighted share of required skills you
   have. Related skills give partial credit (e.g. PostgreSQL counts 60%
   towards SQL).
3. **Career prediction (Module 7):** your profile is scored against 25+
   roles; the best-fitting role's track ladder (9 tracks) is walked to
   estimate your current level, next target role and promotion timeline.
4. **Learning path (Module 9):** missing skills are bucketed into phases
   (Foundation / Core / Advanced / Portfolio) with curated course links and
   week-by-week duration estimates.

## 7. Troubleshooting

| Problem | Fix |
|---------|-----|
| "Could not extract readable text" | The PDF is a scan/image. Save as text-based PDF, DOCX or TXT. |
| Port 5000 already in use | Run `set PORT=5001` (Windows) / `export PORT=5001` (Linux) then `python app.py`. |
| `pip install` fails | Upgrade pip: `python -m pip install --upgrade pip`, ensure Python 3.9+. |
| Charts are empty / CDN errors | Charts load Bootstrap & Chart.js from CDN - internet connection is required. |
| Database errors / wrong schema | Delete `careerai.db` and run `python init_db.py` again. |

## 8. Production Notes

- Set a strong `SECRET_KEY` environment variable before deploying.
- Serve behind a WSGI server (e.g. `waitress-serve --port=8000 app:app`).
- The default SQLite database is fine for demos and coursework; switch
  `SQLALCHEMY_DATABASE_URI` in `config.py` for PostgreSQL/MySQL if needed.
