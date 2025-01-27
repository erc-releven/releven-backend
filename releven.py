from fastapi import FastAPI, Query
from os import path
from rdfproxy import Page, QueryParameters, SPARQLModelAdapter
from typing import Annotated

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from git import Repo


# The automatic health check endpoint is /. The return code has to be 200 or 30x.
@app.get("/")
def version():
    repo = Repo(search_parent_directories=True)
    return {"version": repo.git.describe(tags=True, dirty=True, always=True)}


from releven_location import Location_Location as foo


@app.get("/location")
def location(params: Annotated[QueryParameters, Query()]) -> Page[foo]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_location.rq")
        .read()
        .replace("\n ", " "),
        model=foo,
    )
    return adapter.query(params)


from releven_person import Person_Person as foo


@app.get("/person")
def person(params: Annotated[QueryParameters, Query()]) -> Page[foo]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_person.rq")
        .read()
        .replace("\n ", " "),
        model=foo,
    )
    return adapter.query(params)


from releven__person_stub import PersonStub_Person as foo


@app.get("/person_stub")
def _person_stub(params: Annotated[QueryParameters, Query()]) -> Page[foo]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven__person_stub.rq")
        .read()
        .replace("\n ", " "),
        model=foo,
    )
    return adapter.query(params)


from releven_written_work import WrittenWork_WrittenWork as foo


@app.get("/written_work")
def written_work(params: Annotated[QueryParameters, Query()]) -> Page[foo]:
    adapter = SPARQLModelAdapter(
        target="https://graphdb.r11.eu/repositories/RELEVEN",
        query=open(f"{path.dirname(path.realpath(__file__))}/releven_written_work.rq")
        .read()
        .replace("\n ", " "),
        model=foo,
    )
    return adapter.query(params)
