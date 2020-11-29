FROM thinkwhere/gdal-python:3.7-shippable
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install -r requirements.txt
COPY . /code/
