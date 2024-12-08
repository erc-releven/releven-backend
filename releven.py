from os import path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from git import Repo
from rdfproxy import Page, QueryParameters, SPARQLModelAdapter
from releven_location import Location
from releven_person import Person
from releven_written_work import WrittenWork

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


@app.get("/location")
def location(page: int = 1, size: int = 10) -> Page[Location]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_location.rq")
        .read()
        .replace("\n ", " "),
        model=Location,
    )
    parameters = QueryParameters(page=page, size=size)
    return adapter.query(parameters)


@app.get("/person")
def person(page: int = 1, size: int = 10) -> Page[Person]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_person.rq")
        .read()
        .replace("\n ", " "),
        model=Person,
    )
    parameters = QueryParameters(page=page, size=size)
    return adapter.query(parameters)


@app.get("/written_work")
def written_work(page: int = 1, size: int = 10) -> Page[WrittenWork]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_written_work.rq")
        .read()
        .replace("\n ", " "),
        model=WrittenWork,
    )
    parameters = QueryParameters(page=page, size=size)
    return adapter.query(parameters)
