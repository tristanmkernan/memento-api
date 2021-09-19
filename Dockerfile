FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/
COPY .env.prod /code/.env

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]
