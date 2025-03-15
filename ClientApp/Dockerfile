FROM ubuntu

RUN apt-get update
RUN apt install python3 -y
RUN apt-get install -y python3-pip python3-flask python3-requests

COPY main.py /opt/main.py

EXPOSE 5000

ENTRYPOINT ["python3", "/opt/main.py"]
