FROM python:3.7

WORKDIR /app

COPY divide.py .

VOLUME /data

RUN mkdir -p /data

RUN touch /data/output.txt

RUN echo "0" > /data/output.txt

ENTRYPOINT ["python","./divide.py"]