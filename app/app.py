import os
from flask import Flask, jsonify, request
from .models import db, Item

def create_app():
    app = Flask(__name__)

    # Läs DB-uppgifter från env (sätts av docker-compose)
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_pwd = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_host = os.getenv("POSTGRES_HOST", "db")  # service-namnet i compose
    db_name = os.getenv("POSTGRES_DB", "appdb")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Flask 3: Skapa tabeller i en app context vid uppstart (ersätter before_first_request)
    with app.app_context():
        db.create_all()

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
