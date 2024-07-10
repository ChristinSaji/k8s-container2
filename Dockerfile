FROM python:3.9-slim

WORKDIR /app

COPY app2.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "app2.py"]
