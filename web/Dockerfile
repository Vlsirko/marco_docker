FROM python:3.5
RUN mkdir /web
WORKDIR /web
RUN apt-get update && apt-get install -y mysql-client cron
RUN pip install django \
            uwsgi \
            PyMySql \
            pillow \
            django-mptt \
            django_mptt_admin \
            djangorestframework \
            djangorestframework-filters \
            django-tinymce \
            python-memcached \
            django-dbbackup \
            djangorestframework-recursive \
            djangorestframework-word-filter
ADD . /web
RUN cat cron.config >> /etc/crontab
RUN cron
