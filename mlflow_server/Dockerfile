FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3-pip && pip3 install mlflow

RUN mlflow ui &