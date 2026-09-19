"""
models.py
Database models for CareerAI.

Tables
------
User               -> Module 1  (Registration & Login)
Resume             -> Module 2  (Resume Upload & Parsing)
ExtractedSkill     -> Module 3  (Resume Skill Extraction)
Job                -> Module 4  (Job Description Analysis / job store)
GapAnalysis        -> Module 5  (Skill Matching & Gap Analysis)
GapAnalysis items  -> Module 6  (Skill Gap Recommendation, via stored JSON)
CareerPrediction   -> Module 7  (Career Path Prediction)
LearningPathRecord -> Module 9  (Personalized Learning Path)
ActivityLog        -> Module 12 (Admin analytics)
(Module 8 Job Role Recommendation and Module 10 Job Recommendation are
 computed on the fly from the skill knowledge base and the Job table.)
"""
from datetime import datetime, timezone

from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


def utcnow():
    """Naive UTC timestamp (SQLite friendly, warning free on Python 3.12)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


# --------------------------------------------------------------------------
# Module 1: User Registration & Login
# --------------------------------------------------------------------------
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")  # user | admin
    is_active_user = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=utcnow)

    resumes = db.relationship(
        "Resume", back_populates="owner", cascade="all, delete-orphan", lazy=True
    )
    gap_analyses = db.relationship(
        "GapAnalysis", back_populates="user", cascade="all, delete-orphan", lazy=True
    )
    career_predictions = db.relationship(
        "CareerPrediction", back_populates="user", cascade="all, delete-orphan", lazy=True
    )
    learning_paths = db.relationship(
        "LearningPathRecord", back_populates="user", cascade="all, delete-orphan", lazy=True
    )

    # ---- password helpers -------------------------------------------------
    def set_password(self, raw):
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.password_hash, raw)

    @property
    def is_active(self):
        """Flask-Login compatibility (uses is_active_user column)."""
        return self.is_active_user

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"


@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(User, int(user_id))
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# Module 2: Resume Upload & Parsing
# --------------------------------------------------------------------------
class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    original_filename = db.Column(db.String(255), nullable=False)
    stored_filename = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    raw_text = db.Column(db.Text, nullable=False, default="")

    # parsed fields
    candidate_name = db.Column(db.String(120))
    candidate_email = db.Column(db.String(180))
    candidate_phone = db.Column(db.String(40))
    experience_years = db.Column(db.Float, default=0.0)

    created_at = db.Column(db.DateTime, default=utcnow)

    owner = db.relationship("User", back_populates="resumes")
    skills = db.relationship(
        "ExtractedSkill", back_populates="resume", cascade="all, delete-orphan", lazy=True
    )

    @property
    def skill_count(self):
        return len(self.skills)

    def __repr__(self):
        return f"<Resume #{self.id} {self.original_filename}>"


# --------------------------------------------------------------------------
# Module 3: Resume Skill Extraction
# --------------------------------------------------------------------------
class ExtractedSkill(db.Model):
    __tablename__ = "extracted_skills"

    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey("resumes.id"), nullable=False, index=True)
    skill_name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    frequency = db.Column(db.Integer, default=1)
    proficiency = db.Column(db.Integer, default=60)  # 0-100 estimated

    resume = db.relationship("Resume", back_populates="skills")

    def __repr__(self):
        return f"<Skill {self.skill_name} ({self.proficiency})>"


# --------------------------------------------------------------------------
# Module 4: Job store (Job Description Analysis)
# --------------------------------------------------------------------------
class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    company = db.Column(db.String(160), nullable=False)
    location = db.Column(db.String(160), default="Not specified")
    job_type = db.Column(db.String(40), default="Full-time")
    experience_level = db.Column(db.String(40), default="Entry level")
    category = db.Column(db.String(80), default="Software Development")
    salary_range = db.Column(db.String(80), default="Not disclosed")
    description = db.Column(db.Text, nullable=False)
    skills_text = db.Column(db.Text, default="")            # raw "skills" line
    skills_json = db.Column(db.JSON, default=dict)          # {skill: weight}
    min_experience = db.Column(db.Float, default=0.0)
    is_active = db.Column(db.Boolean, default=True)
    posted_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=utcnow)

    gap_analyses = db.relationship("GapAnalysis", back_populates="job", lazy=True)

    @property
    def required_skills_sorted(self):
        if not self.skills_json:
            return []
        return sorted(self.skills_json.items(), key=lambda kv: kv[1], reverse=True)

    def __repr__(self):
        return f"<Job {self.title} @ {self.company}>"


# --------------------------------------------------------------------------
# Module 5 + 6: Skill Matching & Gap Analysis (+ stored recommendations)
# --------------------------------------------------------------------------
class GapAnalysis(db.Model):
    __tablename__ = "gap_analyses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=True)
    job_title = db.Column(db.String(160), nullable=False)
    company = db.Column(db.String(160), default="")

    match_percentage = db.Column(db.Float, default=0.0)
    verdict = db.Column(db.String(60), default="")
    matched_skills = db.Column(db.JSON, default=list)     # [{skill, weight, proficiency, via}]
    missing_skills = db.Column(db.JSON, default=list)     # [{skill, weight, priority}]
    additional_skills = db.Column(db.JSON, default=list)  # [skill, ...]
    created_at = db.Column(db.DateTime, default=utcnow)

    user = db.relationship("User", back_populates="gap_analyses")
    job = db.relationship("Job", back_populates="gap_analyses")

    def __repr__(self):
        return f"<GapAnalysis u{self.user_id} j{self.job_id} {self.match_percentage}%>"


# --------------------------------------------------------------------------
# Module 7: Career Path Prediction
# --------------------------------------------------------------------------
class CareerPrediction(db.Model):
    __tablename__ = "career_predictions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    best_track = db.Column(db.String(120), default="")
    current_level_title = db.Column(db.String(160), default="")
    next_level_title = db.Column(db.String(160), default="")
    predictions = db.Column(db.JSON, default=dict)
    created_at = db.Column(db.DateTime, default=utcnow)

    user = db.relationship("User", back_populates="career_predictions")


# --------------------------------------------------------------------------
# Module 9: Personalized Learning Path
# --------------------------------------------------------------------------
class LearningPathRecord(db.Model):
    __tablename__ = "learning_paths"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    target_role = db.Column(db.String(160), nullable=False)
    readiness = db.Column(db.Float, default=0.0)
    estimated_duration = db.Column(db.String(60), default="")
    path_data = db.Column(db.JSON, default=dict)
    created_at = db.Column(db.DateTime, default=utcnow)

    user = db.relationship("User", back_populates="learning_paths")


# --------------------------------------------------------------------------
# Module 12: Activity log for admin analytics
# --------------------------------------------------------------------------
class ActivityLog(db.Model):
    __tablename__ = "activity_log"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    user_name = db.Column(db.String(120), default="")
    action = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(255), default="")
    created_at = db.Column(db.DateTime, default=utcnow, index=True)


def log_activity(user, action, details=""):
    """Small helper used across modules to feed the admin dashboard."""
    try:
        entry = ActivityLog(
            user_id=user.id if user else None,
            user_name=user.name if user else "Anonymous",
            action=action,
            details=details[:255],
        )
        db.session.add(entry)
        db.session.commit()
    except Exception:
        db.session.rollback()
