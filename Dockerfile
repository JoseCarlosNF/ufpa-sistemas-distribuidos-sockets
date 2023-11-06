FROM python:3.11-alpine

WORKDIR /app

COPY app/ .

ENV NUM_SOCKETS=10

CMD ["python", "."]
