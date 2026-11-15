from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    response = client.get("/add?num1=10&num2=20")

    assert response.status_code == 200
    assert response.json()["addition"] == 30


def test_negative():
    response = client.get("/add?num1=-10&num2=-20")

    assert response.json()["addition"] == -30


def test_decimal():
    response = client.get("/add?num1=10.5&num2=20.5")

    assert response.json()["addition"] == 31.0