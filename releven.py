from fastapi import FastAPI
from os import path
from rdfproxy import Page, SPARQLModelAdapter

app = FastAPI()

from releven_person import Person
@app.get("/person/")
def person(page : int = 1, size : int = 10):
  adapter = SPARQLModelAdapter(
    target="https://graphdb.r11.eu/repositories/RELEVEN",
    query=open(f"{path.dirname(path.realpath(__file__))}/releven_person.rq").read().replace('\n ', ' '),
    model=Person)
  return adapter.query(page=page, size=size)
