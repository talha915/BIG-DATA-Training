from fastapi.testclient import TestClient
import pytest
from app.index import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPIs!"}