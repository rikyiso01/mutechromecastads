FROM docker.io/python:3.10.14-alpine3.19

RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --only main --no-root
COPY mutechromecastads.py /app/
CMD ["poetry","run","python","mutechromecastads.py"]
