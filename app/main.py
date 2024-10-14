import asyncio
from fastapi import FastAPI
import uvicorn

# from app.database.database import create_database
from app.database.database import create_tables
from app.deposite.deposite_hendlers import router as deposit_router

def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/api/docs',
        title='Deposit Calculate v1',
    )
    app.include_router(deposit_router)

    return app


if __name__ == "__main__":
    asyncio.run(create_tables())
    uvicorn.run(app="main:create_app", factory=True, reload=True)
    # export PYTHONPATH="/home/kvezac/mente/calculate_deposit"
