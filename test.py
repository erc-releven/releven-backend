import pytest
from fastapi.testclient import TestClient

from releven import app

client = TestClient(app)


def test_read_debug():
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.skip(reason="might fail due to network timeouts")
def test_read_counts():
    response = client.get("/counts")
    assert response.status_code == 200
