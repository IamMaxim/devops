FROM python:3.9.6-bullseye

WORKDIR /app
ENV PYTHONUNBUFFERED 1
#ENV DJANGO_SETTINGS_MODULE timeserver.settings

# Install Python dependencies
RUN python -m pip install -U --force-reinstall pip
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

WORKDIR /app/src

CMD (python manage.py migrate && \
     echo yes | python manage.py collectstatic && \
     python manage.py runserver 0.0.0.0:8000)
#     uwsgi uwsgi.ini)