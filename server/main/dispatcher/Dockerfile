FROM python:3.10

COPY . /usr/src/dispatcher

WORKDIR /usr/src/dispatcher

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN python -m grpc_tools.protoc -I./grpc --python_out=. --grpc_python_out=. ./grpc/dispatcher.proto

CMD ["python", "-u", "dispatcher.py"]

