FROM python:3.14

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests

CMD ["python", "client.py"]