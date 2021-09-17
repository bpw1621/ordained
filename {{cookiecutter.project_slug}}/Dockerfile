FROM {{cookiecutter.base_image}}
LABEL maintainer="{{cookiecutter.full_name}} <{{cookiecutter.email}}>"

WORKDIR /usr/src/app
COPY .. .
RUN pip install -U pip && pip install --no-cache-dir -e .