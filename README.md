# releven-backend

Build and run a container locally:

```bash
docker build -t releven-backend .
docker run -p 8000:5000 releven-backend
```

Run locally with `uv`:
```bash
uv sync
uv run fastapi dev releven.py --port 8000
```
