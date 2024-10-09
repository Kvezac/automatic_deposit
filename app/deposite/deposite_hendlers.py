# from .deposite_schema import DepositeSchema


from fastapi import APIRouter

from .deposite_schema import DepositeSchema


router = APIRouter(prefix='/deposit', tags=['Deposit Get Info'])


@router.get('/all', response_model=list[DepositeSchema])
def get_deposits():
    return {"get_deposits": "get_deposits"}


@router.get('/{id}')
def get_deposit():
    return {"get_deposit": "get_deposits"}



@router.post('/')
def create_deposit():
    return {"create_deposit": "create_deposit"}
