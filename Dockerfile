FROM python:3.8.3 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.8.3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /usr/src/app/

RUN chmod 755 /usr/src/app/prestart.sh









#FROM python:3.8
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /usr/src/dm_rest
#
#COPY ./req.txt /usr/src/req.txt
#RUN pip install -r /usr/src/req.txt
#
#COPY . /usr/src/dm_rest
#
#EXPOSE 8000

