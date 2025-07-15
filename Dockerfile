# Usamos una imagen oficial de Python
FROM python:3.11-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos requirements
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY app/ .

# Exponemos el puerto
EXPOSE 5000

# Comando para correr la app
CMD ["python", "main.py"]
