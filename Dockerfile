FROM python:3.11-slim

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.main:app", "--reload"]
