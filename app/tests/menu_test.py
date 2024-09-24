from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_generate_menu():
    response = client.post("/generate-menu/", json={
        "optional_dish": "duck confit",
        "ingredients": ["duck", "thyme", "garlic"],
        "supplies": ["pan", "oven"]
    })
    assert response.status_code == 200
    assert response.json()['MenuItem']['Name'] == "duck confit"
