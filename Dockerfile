FROM python:3.12.2-slim
LABEL authors="pieceowater"

RUN useradd -m python-user

WORKDIR /app

COPY requirements.txt .

USER python-user

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "main.py"]
