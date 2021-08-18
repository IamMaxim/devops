FROM python:3.9.6-bullseye

WORKDIR /app
ENV PYTHONUNBUFFERED 1

# Install Python dependencies
RUN python -m pip install -U --force-reinstall pip
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

RUN (
  python -m django migrate && \
  python -m django collectstatic && \
  uwsgi uwsgi.ini
)