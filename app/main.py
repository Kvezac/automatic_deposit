from fastapi import FastAPI
import uvicorn

<<<<<<< HEAD
from deposite.deposite_hendlers import router as deposit_router
=======
from app.deposite.deposite_hendlers import router as deposit_router
>>>>>>> 25c9873 ( On branch developer)

DATE_FORMAT = '%d.%m.%Y'

def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/api/docs',
        title='Deposit Calculate v1',
    )
    app.include_router(deposit_router)

    return app


if __name__ == "__main__":
    uvicorn.run(app="main:create_app", factory=True, reload=True)
