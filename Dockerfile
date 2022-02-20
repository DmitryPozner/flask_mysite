FROM python:3.8
MAINTAINER Dmitry Pozner "dmitrypozner@dgp.ru"
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["application.py"]
