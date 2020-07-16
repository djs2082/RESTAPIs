From python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /coronadata
WORKDIR /coronadata
ADD . /coronadata
RUN pip3 install -r requirements.txt
