FROM python:3.7-alpine

RUN mkdir /opt/skel
WORKDIR /opt/skel

COPY requirements.txt .
COPY *.py ./
COPY config/config.json /etc/skel-python-service/config.json
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /usr/src/app/log

CMD ["python3", "./app.py"]