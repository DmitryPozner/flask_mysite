FROM ubuntu:latest
MAINTAINER Dmitry Pozner "dmitrypozner@dgp.ru"
WORKDIR /app
COPY . .
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python3-dev build-essential python3-pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["application.py"]
