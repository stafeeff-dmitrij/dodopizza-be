FROM python:3.11-slim

COPY requirements/base.txt /src/requirements/base.txt
COPY requirements/prod.txt /src/requirements/prod.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements/prod.txt

COPY ./src /src
COPY ./scripts/api.sh /docker/api.sh
COPY ./pyproject.toml /pyproject.toml

RUN chmod a+x /docker/*.sh
