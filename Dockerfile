FROM python:3.9

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod +x exeScript.sh

CMD ["./exeScript.sh"]
