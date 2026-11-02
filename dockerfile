#imagen base de Python
FROM python:3.12-slim

#carpeta de trabajo dentro del contenedor
WORKDIR /app

#copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copiar la API y el modelo entrenado
COPY app/ ./app/
COPY modelo/ ./modelo/

#puerto que utilizará la API
EXPOSE 8000

#iniciar la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]