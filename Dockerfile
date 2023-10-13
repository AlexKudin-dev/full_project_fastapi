FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x command.sh

RUN chmod a+x test_main.py

CMD gunicorn main:app  --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker
