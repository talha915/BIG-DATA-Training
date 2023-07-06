from fastapi.testclient import TestClient
import pytest
from app.index import main

client = TestClient(main)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}