from fastapi import FastAPI
import uvicorn

from app.deposite.deposite_hendlers import router as deposit_router

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
