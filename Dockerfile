FROM python:3.11-slim

EXPOSE 8081

RUN mkdir -p /opt/dionisiosantiago
WORKDIR /opt/dionisiosantiago

COPY . .

#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "siteDjango.wsgi:application", "--bind", "0.0.0.0:8081"]
