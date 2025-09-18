from fastapi.testclient import TestClient

from releven import app

client = TestClient(app)


def test_read_counts():
    response = client.get("/counts")
    assert response.status_code == 200
