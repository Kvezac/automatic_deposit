# from .deposite_schema import DepositeSchema


from fastapi import APIRouter

<<<<<<< HEAD
from deposite.deposite_service import calculate_deposit
=======

from app.deposite.deposite_service import calculate_deposit
>>>>>>> 25c9873 ( On branch developer)
from tests.fixture import DATA

from .deposite_schema import DepositCreationSchema, DepositSchema


router = APIRouter(prefix='/deposit', tags=['Deposit Get Info'])



router = APIRouter(prefix='/crud', tags=['CRUD'])


@router.get('/all', response_model=list[DepositSchema])
async def get_all_items():
    [print(f'[INFO GET ALL]:  {value}') for value in DATA]
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

    print(f'[INFO POST]: {new_id} {new_deposit} ')
    results: dict[str, float] = calculate_deposit(new_deposit)
    return results
