FROM python:3
WORKDIR /src/usr/app
COPY requirments.txt ./src/usr/app
RUN pip install requirments.txt
COPY . .
