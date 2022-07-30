# set base image (host OS)
FROM python:3.9-slim

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# set the working directory in the container
WORKDIR /code

COPY ./customers/requirements.txt ./
COPY ./protos ./protos
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY ./customers/start.sh ./
RUN chmod +x ./start.sh
# copy the content of the local src directory to the working directory
COPY ./customers/app ./app

ADD ./customers/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["./start.sh"]
