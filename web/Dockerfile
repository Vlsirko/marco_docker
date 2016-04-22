FROM python:3.5
RUN mkdir /web
WORKDIR /web
RUN pip install django PyMySql pillow django-mptt django_mptt_admin djangorestframework gunicorn
ADD . /web