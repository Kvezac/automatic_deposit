from fastapi import APIRouter


from app.deposite.deposite_service import calculate_deposit
from tests.fixture import DATA

from .deposite_schema import DepositCreationSchema, DepositSchema


router = APIRouter(prefix='/deposit', tags=['Deposit Get Info'])



router = APIRouter(prefix='/deposit', tags=['DEPOSIT Get Info'])


@router.get('/all', response_model=list[DepositSchema])
async def get_all_items():
    return DATA


@router.get('/{id}')
async def get_item(id: int) -> dict[str, float]:
    item = [value for value in DATA if value['id'] == id][0]
    results: dict[str, float] = calculate_deposit(DepositSchema(**item))
    return results

@router.post('/create')
async def create_item(body: DepositCreationSchema):
    new_id = len(DATA) + 1
    new_deposit = DepositSchema(id=new_id, **body.dict())
    DATA.append(new_deposit) # type: ignore
    results: dict[str, float] = calculate_deposit(new_deposit)
    return results
