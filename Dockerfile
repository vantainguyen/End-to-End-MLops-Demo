FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN sudo apt update -y && sudo apt install awscli -y && sudo apt install python3-pip

RUN sudo apt-get update && pip install -r requirements.txt

RUN chmod +x exeScript.sh

CMD ["./exeScript.sh"]