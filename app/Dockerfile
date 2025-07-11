# Imagen base
FROM python:3.11-slim

# Crear un directorio de trabajo
WORKDIR /app

# Copiar requirements y app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Usuario no root (opcional pero recomendado)
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Exponer puerto de Flask
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]
