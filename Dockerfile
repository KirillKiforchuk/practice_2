FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    libffi-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN apt-get purge -y gcc

EXPOSE 8001

ENTRYPOINT  ["honcho", "start", "--no-colour", "--no-prefix"]
