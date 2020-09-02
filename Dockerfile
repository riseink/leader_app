FROM python:3.6-slim

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev postgresql-client curl git \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get update && apt-get install -y nodejs && apt-get install -y npm

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
COPY package.json /app/

RUN pip install -r requirements.txt \
    && npm i npm@latest -g \
    && npm install


# Install private packages
# COPY ./src /app/src

# Using method from this blog post to get around docker's limitations
# with python local packages:
# https://thekev.in/blog/2016-11-18-python-in-docker/index.html
# WORKDIR /app/src
# package directories need to be added to PYTHONPATH. This value is passed as a
# build arg in install.sh
# ARG PYTHONPATH
# ENV PYTHONPATH=$PYTHONPATH
# Iterate through each directory and install any with a setup.py file
# RUN for D in */; do \
#         if [ -f "${D}setup.py" ]; then \
#             cd /usr/local/lib/python3.6/site-packages; \
#             python "/app/src/${D}setup.py" develop --no-deps; \
#             cd /app/src; \
#         fi; \
#     done

# Set AWS environment variables
ARG AWS_STORAGE_BUCKET_NAME
ENV AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME
ARG AWS_ACCESS_KEY_ID
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

COPY . /app
WORKDIR /app
