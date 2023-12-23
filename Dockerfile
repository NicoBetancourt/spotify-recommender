FROM python:3.10-slim-buster as base
FROM base as deploy

WORKDIR /usr/app
COPY [ "requirements.txt", "./" ]
RUN pip install -r requirements.txt
COPY ["./app/", "./app/"]
ENTRYPOINT [ "python" ]
CMD ["app/app.py"]

