FROM python:3.10.14-alpine3.18
WORKDIR /usr/src/app

RUN apk add --no-cache bash

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ./start.sh