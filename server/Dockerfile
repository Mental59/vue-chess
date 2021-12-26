FROM python:3.6

RUN pip install grpcio
RUN pip install grpcio-tools

COPY ./test/ /usr/src/test_server/
WORKDIR /usr/src/test_server/

CMD ["python", "server.py"]