FROM python:3.12-slim
ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

WORKDIR /app/

COPY . /app

# Create the user and install all dependencies
# Declare the /app directory as a safe for any git operations, like reading the revision and tag
# Reset the git repository to the last commit as otherwise
# the image will report as dirty if build on windows due to the line endings.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt update && apt -y full-upgrade && apt install -y git && pip3 install uv && apt clean \
    && uv sync && ./generate-endpoints.sh \
    && uv run pytest test.py \
    && git config --system --add safe.directory /app \
    && cd /app && git reset --hard

USER app

CMD ["uv", "run", "fastapi", "run", "releven.py", "--port", "5000", "--proxy-headers"]

EXPOSE 5000
