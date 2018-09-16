FROM python:3.6.6-alpine3.8

RUN apk update && apk add dos2unix

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
 && rm -f /tmp/requirements.txt

RUN mkdir /app
COPY attemptproj/ /app/attemptproj
COPY attemptapp/ /app/attemptapp
COPY manage.py /app/manage.py
COPY testservice.sh /testservice.sh
COPY runservice.sh /runservice.sh

RUN chmod +x /testservice.sh /runservice.sh \
 && dos2unix /testservice.sh /runservice.sh

CMD /runservice.sh