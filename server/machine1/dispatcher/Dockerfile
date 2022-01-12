FROM ubuntu

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install git python3-pip

COPY . /usr/src/dispatcher

WORKDIR /usr/src/dispatcher

# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN python3 -m grpc_tools.protoc -I./grpc --python_out=. --grpc_python_out=. ./grpc/dispatcher.proto

CMD ["python3", "-u", "dispatcher.py"]

