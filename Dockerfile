FROM python:3.9

WORKDIR /app

COPY . .

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD gunicorn main:app  --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker
