from app.deposite.deosite_models import Deposit
import pytest
from fastapi.testclient import TestClient
from app.main import create_app
from app.database.database import SessionLocal



client = TestClient(create_app())

# Dependency override for testing
@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(scope="module")
def create_deposit(db_session):
    # Create a test deposit entry
    deposit = Deposit(periods=12, amount=1000.0, rate=5.0)
    db_session.add(deposit)
    db_session.commit()
    db_session.refresh(deposit)
    return deposit


def test_get_all_items(db_session):
    response = client.get("/deposit/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item(create_deposit):
    response = client.get(f"/deposit/{create_deposit.id}")
    assert response.status_code == 200
    assert "result" in response.json()


def test_create_item():
    new_deposit_data = {
        "periods": 12,
        "amount": 2000.0,
        "rate": 4.5,
    }

    response = client.post("/deposit/create", json=new_deposit_data)

    assert response.status_code == 200
    assert "result" in response.json()
