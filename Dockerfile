FROM python:3.11.10

ENV PYTHONDONTWRIEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry lock --no-update
RUN poetry config virtualenvs.create false
RUN poetry add uvicorn
RUN poetry install


EXPOSE 8000

COPY ./app /app

CMD ["poetry", "run", "uvicorn", "main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--reload"]
