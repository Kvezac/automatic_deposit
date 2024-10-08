from fastapi import FastAPI
import uvicorn

def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/api/docs',
        title='Deposit Calculate v1',
    )

    return app


if __name__ == "__main__":
    uvicorn.run(app="main:create_app", factory=True, reload=True)
