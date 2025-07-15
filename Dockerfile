FROM python:3.10-slim

EXPOSE 8081

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /siteDjango

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

COPY siteDjango/ .

RUN python3 manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]

