FROM python:3.9.6-bullseye
MAINTAINER iammaxim

WORKDIR /app

# Required for proper stdout output in Docker.
ENV PYTHONUNBUFFERED 1

# Disable Django's debug mode in production image.
# Use local environment for testing.
ENV DEBUG=false

# Disable root user for security purposes.
RUN adduser deploy

# Install Python dependencies.
RUN python -m pip install -U --force-reinstall pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy only source folder, excluding non-required stuff.
COPY ./src /app/src
# We need to run chown before changing the user.
RUN chown -R deploy:deploy /app/src
USER deploy

WORKDIR /app/src

EXPOSE 8000

CMD (python manage.py migrate && \
     echo yes | python manage.py collectstatic && \
     python manage.py runserver 0.0.0.0:8000)
