import os
from flask import Flask, jsonify, request
from .models import db, Item


def create_app():
    app = Flask(__name__)

    # --- Database configuration ---
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_pwd = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_name = os.getenv("POSTGRES_DB", "appdb")

    # Use localhost in GitHub Actions CI
    if os.getenv("GITHUB_ACTIONS") == "true":
        db_host = "localhost"

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{db_user}:{db_pwd}@{db_host}:5432/{db_name}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # Create tables on startup (Flask 3 removed before_first_request)
    with app.app_context():
        db.create_all()

    # --- Routes ---
    @app.get("/")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/items")
    def list_items():
        items = Item.query.order_by(Item.id.desc()).all()
        return jsonify([i.to_dict() for i in items]), 200

    @app.post("/items")
    def create_item():
        data = request.get_json(force=True, silent=True) or {}
        title = data.get("title")
        if not title:
            return jsonify({"error": "Missing 'title'"}), 400
        item = Item(title=title)
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201

    return app


# Flask entrypoint ("--app app.app")
app = create_app()
