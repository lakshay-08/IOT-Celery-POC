FROM python:3.12
WORKDIR /app
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY worker.py tasks.py
CMD ["python", "worker.py"]