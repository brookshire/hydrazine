FROM python:3
ENV PYTHONUNBUFFERED 1
ENV http_proxy http://proxy.houston.hpecorp.net:8080
ENV https_proxy http://proxy.houston.hpecorp.net:8080
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt