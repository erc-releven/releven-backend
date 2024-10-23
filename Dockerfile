FROM python:3.12
ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt update
RUN apt install git
RUN pip3 install poetry

WORKDIR /app/

COPY . /app
RUN poetry config virtualenvs.create false && poetry install --no-dev

USER app

CMD ["fastapi", "run", "releven.py"]

EXPOSE 8000
