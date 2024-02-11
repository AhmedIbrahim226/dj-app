# FROM python:3.10

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /dj-app

# COPY requirements.txt .

# # To running based on DOCKERIZE_TYPE value from docker-compose files 
# ARG DOCKERIZE_TYPE
# RUN if ["${DOCKERIZE_TYPE}" = "production"]; \
#     then pip install -r requirements.txt; \
#     else pip install -r requirements.txt; \
#     fi

# COPY . .

# EXPOSE 8000

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.10 as base

FROM base as development

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /dj-app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]


FROM base as production

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /dj-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
