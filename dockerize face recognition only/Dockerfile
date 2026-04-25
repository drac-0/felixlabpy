FROM python:3.11-slim

ADD facerecog_doorlock.py .

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD facerecog_doorlock.py .
ADD p.jpeg .

RUN pip install opencv-python face_recognition
    
CMD ["python", "./facerecog_doorlock.py"]
