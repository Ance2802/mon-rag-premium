FROM python:3.12-slim
WORKDIR /app

# Installation des outils de compilation nécessaires pour ChromaDB
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]