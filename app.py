"""
app.py
CareerAI - AI-Based Resume-Job Skill Gap & Career Path Prediction System
Flask application factory & entry point.

Run:
    python init_db.py     # first time only (creates DB + seeds data)
    python app.py         # starts http://127.0.0.1:5000
"""
from pathlib import Path

from flask import Flask

from config import Config
from extensions import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Path(Config.UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

    # --- extensions --------------------------------------------------------
    db.init_app(app)
    login_manager.init_app(app)

    # --- blueprints --------------------------------------------------------
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.resume import resume_bp
    from routes.jobs import jobs_bp
    from routes.analysis import analysis_bp
    from routes.dashboard import dashboard_bp
    from routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)

    # --- error handlers ----------------------------------------------------
    @app.errorhandler(404)
    def not_found(e):
        return render_error(404, "Page not found", "The page you requested does not exist.")

    @app.errorhandler(403)
    def forbidden(e):
        return render_error(403, "Access denied", "You do not have permission to view this page.")

    @app.errorhandler(413)
    def too_large(e):
        return render_error(413, "File too large", "Maximum upload size is 8 MB.")

    @app.errorhandler(500)
    def server_error(e):
        return render_error(500, "Something went wrong", "An unexpected error occurred. Please try again.")

    def render_error(code, title, message):
        from flask import render_template
        return render_template("error.html", code=code, title=title, message=message), code

    # --- template helpers --------------------------------------------------
    from skills_data import CATEGORY_COLORS

    @app.context_processor
    def inject_globals():
        return {"CATEGORY_COLORS": CATEGORY_COLORS}

    @app.template_filter("monthname")
    def monthname(dt):
        return dt.strftime("%b %d, %Y") if dt else ""

    # --- database tables ---------------------------------------------------
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    port = int(__import__("os").environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
