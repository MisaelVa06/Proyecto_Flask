# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto que usará Flask
EXPOSE 5000

# Ejecuta el servidor Flask directamente con Python
CMD ["python", "app.py"]