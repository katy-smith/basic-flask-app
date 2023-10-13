# syntax=docker/dockerfile:1.5
FROM python:3.10-alpine AS builder

WORKDIR /src
COPY requirements.txt /src/requirements.txt 
COPY flask/gunicorn_config.py /src/gunicorn_config.py
COPY /nginx/* /tmp

RUN  pip3 install -r requirements.txt

COPY /flask .

EXPOSE 9090

CMD ["gunicorn", "--config", "gunicorn_config.py", "server:application"]
FROM builder as dev-envs

EXPOSE 9090

RUN apk update apk add git

RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["gunicorn", "--config", "gunicorn_config.py", "server:application"]
