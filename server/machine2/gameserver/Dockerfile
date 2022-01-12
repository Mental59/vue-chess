FROM ubuntu

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install git python3-pip

COPY . /usr/src/gameserver

WORKDIR /usr/src/gameserver

# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python3", "-u", "gameserver.py"]