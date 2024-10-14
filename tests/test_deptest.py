from app.deposite.deosite_models import Deposit
import unittest
from fastapi.testclient import TestClient
from app.main import create_app
from app.database.database import SessionLocal


class TestDepositAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(create_app())
        cls.db = SessionLocal()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def setUp(self):
        # Create a test deposit entry before each test
        self.deposit = Deposit(periods=12, amount=1000.0, rate=5.0)
        self.db.add(self.deposit)
        self.db.commit()
        self.db.refresh(self.deposit)

    def tearDown(self):
        # Clean up the database after each test
        self.db.query(Deposit).delete()
        self.db.commit()

    def test_get_all_items(self):
        response = self.client.get("/deposit/all")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_item(self):
        response = self.client.get(f"/deposit/{self.deposit.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("result", response.json())

    def test_create_item(self):
        new_deposit_data = {
            "periods": 12,
            "amount": 2000.0,
            "rate": 4.5,
        }

        response = self.client.post("/deposit/create", json=new_deposit_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("result", response.json())


if __name__ == "__main__":
    unittest.main()
