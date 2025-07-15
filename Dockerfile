FROM python:3.10-slim

EXPOSE 8081

# 1. Criar diretório e definir como diretório de trabalho
WORKDIR /app

# 2. Copiar os arquivos necessários
COPY requirements.txt .

# 3. Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo o restante do projeto
COPY siteDjango/ .

# 5. Rodar collectstatic (agora manage.py já está disponível!)
RUN python3 manage.py collectstatic --noinput

# 6. Rodar o servidor
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]


#Teste de atualização do Dockerfile