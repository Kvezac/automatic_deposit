from abc import ABC, abstractmethod


from sqlalchemy import select
from app.deposite.deosite_models import Deposit

class DepositRepository(ABC):
    @abstractmethod
    def get_deposits(self):
        pass

    # @abstractmethod
    # async def create_deposit(self, deposit: DepositCreate) -> Deposit:
    #     pass
