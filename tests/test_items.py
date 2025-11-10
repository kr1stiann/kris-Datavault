import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.app import create_app, db
from app.models import Item


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_health(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

def test_create_and_list_items(client):
    # create
    res = client.post("/items", json={"title": "Test item"})
    assert res.status_code == 201

    # list
    res = client.get("/items")
    data = res.get_json()
    assert isinstance(data, list)
    assert any(item["title"] == "Test item" for item in data)
