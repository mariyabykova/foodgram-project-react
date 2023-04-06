FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc \
#     && pip install psycopg2
RUN pip3 install -r requirements.txt --no-cache-dir

COPY foodgram/ .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]