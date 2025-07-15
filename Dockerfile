FROM python:3.10-slim

EXPOSE 8081

RUN mkdir -p /opt/dionisiosantiago  
WORKDIR /opt/dionisiosantiago

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY siteDjango/ .

RUN python3 manage.py collectstatic --noinput

COPY . .

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8081"]