FROM python:3.7

WORKDIR /app

COPY multiply.py .

VOLUME /data

RUN mkdir -p /data

RUN touch /data/multiply.txt

ENTRYPOINT ["python","./multiply.py"]