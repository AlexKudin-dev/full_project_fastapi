FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

RUN chmod a+x tests/test_main.py






