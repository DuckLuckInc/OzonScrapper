FROM python:3.8-buster as build
WORKDIR /OzonScrapper
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 runner.py
