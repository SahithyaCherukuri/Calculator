FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

VOLUME /my-volume

ENTRYPOINT ["python","./multiply.py"]