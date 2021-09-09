FROM python:alpine3.8

RUN apk add build-base && apk add sqlite

COPY boot.sh ./
COPY python ./python
COPY requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x boot.sh

ENTRYPOINT ["./boot.sh"]
