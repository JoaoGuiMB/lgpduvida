FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 pip

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]