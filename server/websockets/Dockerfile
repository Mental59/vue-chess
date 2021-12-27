FROM ubuntu

# Add source files to docker image
ADD .	/home/websocket

# Update and install dependencies
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install git python3-pip

# Install project requirements
RUN cd /home/websocket \
    && pip3 install -r requirements.txt

    
EXPOSE 8888

WORKDIR /home/websocket
CMD ["python3", "-u", "python-websockets_websocket-benchmark-server.py"]
