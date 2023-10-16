FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x alembic.sh

RUN chmod a+x app.sh

RUN chmod a+x test_main.py






