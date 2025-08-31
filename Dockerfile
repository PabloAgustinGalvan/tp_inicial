FROM python:3.10-slim

# Instala dependencias del sistema necesarias para compilar dlib
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libx264-dev \
    libxvidcore-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia tu código al contenedor
WORKDIR /app
COPY . /app

# Instala las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto que usás en Flask
EXPOSE 10000

# Comando para iniciar el backend
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]

