# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

WORKDIR /usr/src/app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


COPY . .

ENV FLASH_APP=rest_server.py

CMD flask run --host=0.0.0.0
