FROM python:3.4
RUN apt-get update && apt-get install -y libxmlsec1-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /cod