FROM python:3.11-slim

COPY server.py .

EXPOSE 8080

CMD ["python", "server.py"]
