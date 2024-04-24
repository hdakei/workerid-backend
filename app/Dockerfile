FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -i requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
