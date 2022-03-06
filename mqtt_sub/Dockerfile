# call python image from the hub
FROM python:3.8-slim-buster

#set a vitual directory in the container for the app to run
WORKDIR /app
# copy the requirements
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1883

CMD [ "python", "./mqtt-client-sub.py"] 