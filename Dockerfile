FROM python:3.9
# Send output straight to container log
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --no-cache-dir -r requirements.txt
WORKDIR /code/restaurant-menu
