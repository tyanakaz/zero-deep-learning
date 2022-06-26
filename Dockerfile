FROM python:3.10-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install jupyterlab numpy matplotlib