FROM python:3.5
RUN mkdir /web
WORKDIR /web
RUN pip install django uwsgi PyMySql pillow django-mptt django_mptt_admin djangorestframework  djangorestframework-filters django-tinymce  python-memcached
ADD . /web
