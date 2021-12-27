FROM python:3.10-slim

COPY . /usr/src/gameserver

WORKDIR /usr/src/gameserver

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python", "-u", "gameserver.py"]
