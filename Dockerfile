FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
# this copies all the source code to the /app directory in the container
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]