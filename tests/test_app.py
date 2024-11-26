import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_fetch_random_page(client):
    # Mock request data
    data = {
        "notion_token": "fake_token",
        "database_ids": ["db1", "db2"]
    }
    
    response = client.post("/random-page", json=data)
    
    # Assert response status code and content
    assert response.status_code == 200