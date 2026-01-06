FROM ghcr.io/astral-sh/uv:debian-slim
WORKDIR /app/

COPY . /app

# Create the user and install all dependencies
# Declare the /app directory as a safe for any git operations, like reading the revision and tag
# Reset the git repository to the last commit as otherwise
# the image will report as dirty if build on windows due to the line endings.
RUN apt update && apt -y full-upgrade && apt install -y git && apt clean \
    && uv sync && ./generate-endpoints.sh \
    && uv run pytest test.py \
    && git config --system --add safe.directory /app \
    && cd /app && git reset --hard

CMD ["/app/.venv/bin/fastapi", "run", "releven.py", "--port", "5000", "--proxy-headers"]

EXPOSE 5000
