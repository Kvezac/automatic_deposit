from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from app.deposite.deosite_models import Deposit
from app.database.database import SessionLocal
from app.deposite.deposite_service import calculate_deposit
from .deposite_schema import DepositCreationSchema, DepositSchema

router = APIRouter(prefix='/deposit', tags=['Deposit Get Info'])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # type: ignore

@router.get('/all', response_model=list[DepositSchema])
async def get_all_items(db: Session = Depends(get_db)):
    deposits = db.execute(select(Deposit)).scalars().all()
    return deposits

@router.get('/{id}', response_model=dict[str, float])
async def get_item(id: int, db: Session = Depends(get_db)) -> dict[str, float]:
    deposit = db.execute(select(Deposit).where(Deposit.id == id)).scalar_one_or_none()
    if deposit:
            results: dict[str, float] = calculate_deposit(deposit) # type: ignore
    return results

@router.post('/create', response_model=dict[str, float])
async def create_item(body: DepositCreationSchema, db: Session = Depends(get_db)):
    new_deposit = Deposit(periods=body.periods, amount=body.amount, rate=body.rate)

    # Insert the new deposit into the database
    db.add(new_deposit)
    db.commit()  # Commit the transaction to save changes
    db.refresh(new_deposit)  # Refresh to get the latest state of the object

    # Now we can calculate based on the newly created deposit
    results: dict[str, float] = calculate_deposit(DepositSchema(new_deposit)) # type: ignore
    return results
