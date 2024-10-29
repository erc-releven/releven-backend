FROM python:3.12-slim
ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

WORKDIR /app/

COPY . /app

# Create the user and install all dependencies
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt update && apt -y full-upgrade && apt install -y git && pip3 install poetry && apt clean \
    && poetry config virtualenvs.create false && poetry install --no-dev && poetry cache clear --all . \
    && git config --system --add safe.directory /app

USER app

CMD ["fastapi", "run", "releven.py", "--port", "5000", "--proxy-headers"]

EXPOSE 5000
