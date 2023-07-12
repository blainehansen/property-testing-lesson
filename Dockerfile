FROM python:3.11-buster

RUN pip install pytest
RUN pip install hypothesis

WORKDIR /home

CMD python
