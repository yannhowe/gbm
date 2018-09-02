FROM python:3.6-onbuild

ONBUILD COPY ./requirements/base.txt /usr/src/app/requirements.txt
ONBUILD RUN pip install --no-cache-dir -r requirements.txt