from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import path
from rdfproxy import SPARQLModelAdapter
from git import Repo
from releven_person import Person

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# The automatic health check endpoint is /. The return code has to be 200 or 30x.
@app.get("/")
def version():
    repo = Repo(search_parent_directories=True)
    return {"version": repo.git.describe(tags=True, dirty=True, always=True)}


@app.get("/person")
def person(page: int = 1, size: int = 10):
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_person.rq")
        .read()
        .replace("\n ", " "),
        model=Person,
    )
    return adapter.query(page=page, size=size)
