FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y && apt install python3-pip

RUN apt-get update && pip install -r requirements.txt

RUN chmod +x exeScript.sh

CMD ["./exeScript.sh"]