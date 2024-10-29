from fastapi import FastAPI
from os import path
from rdfproxy import Page, SPARQLModelAdapter
from git import Repo

app = FastAPI()

# The automatic health check endpoint is /. The return code has to be 200 or 30x.
@app.get("/")
def version():
  repo = Repo(search_parent_directories=True)
  return {"version": repo.git.describe(tags=True, dirty=True, always=True)}

from releven_person import Person
@app.get("/person/")
def person(page : int = 1, size : int = 10):
  adapter = SPARQLModelAdapter(
    target="https://graphdb.r11.eu/repositories/RELEVEN",
    query=open(f"{path.dirname(path.realpath(__file__))}/releven_person.rq").read().replace('\n ', ' '),
    model=Person)
  return adapter.query(page=page, size=size)
