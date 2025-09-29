# releven-backend

Docker build and deployment of the RELEVEN project's `wisskas`-generated `rdfproxy` REST backend

- `main` branch is deployed to https://releven-backend.acdh-dev.oeaw.ac.at/docs
- `dev` branch is deployed to https://releven-backend-dev.acdh-dev.oeaw.ac.at/docs

Run locally with `uv`:

```bash
uv sync
./generate-endpoints.sh
uv run fastapi dev releven.py
```

Build and run a container locally:

```bash
docker build -t releven-backend .
docker run -p 8000:5000 releven-backend
```
