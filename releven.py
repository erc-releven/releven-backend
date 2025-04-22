from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from git import Repo
from os import path
from rdfproxy import Page, QueryParameters, SPARQLModelAdapter
from typing import Annotated

from releven_g_external_authority import G_external_authority
from releven_g_person import G_person
from releven_g_bibliography import G_bibliography
from releven_g_written_text import G_written_text
from releven_g_publication import G_publication
from releven_g_seal import G_seal
from releven_g_seal_collection import G_seal_collection
from releven_g_boulloterion import G_boulloterion
from releven_g_author_group import G_author_group
from releven_g_passage import G_passage
from releven_g_ethnic_group import G_ethnic_group
from releven_g_gender import G_gender
from releven_g_social_relationship import G_social_relationship
from releven_g_language import G_language
from releven_g_religious_affiliation import G_religious_affiliation
from releven_g_legal_status import G_legal_status
from releven_g_social_role import G_social_role


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


def load_query(name):
    return (
        open(f"{path.dirname(path.realpath(__file__))}/{name}.rq")
        .read()
        .replace("\n ", " ")
    )


@app.get("/g_external_authority")
def releven_g_external_authority(
    params: Annotated[QueryParameters[G_external_authority], Query()],
) -> Page[G_external_authority]:
    query = load_query("releven_g_external_authority")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_external_authority,
    )
    return adapter.query(params)


@app.get("/g_person")
def releven_g_person(
    params: Annotated[QueryParameters[G_person], Query()],
) -> Page[G_person]:
    query = load_query("releven_g_person")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_person,
    )
    return adapter.query(params)


@app.get("/g_bibliography")
def releven_g_bibliography(
    params: Annotated[QueryParameters[G_bibliography], Query()],
) -> Page[G_bibliography]:
    query = load_query("releven_g_bibliography")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_bibliography,
    )
    return adapter.query(params)


@app.get("/g_written_text")
def releven_g_written_text(
    params: Annotated[QueryParameters[G_written_text], Query()],
) -> Page[G_written_text]:
    query = load_query("releven_g_written_text")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_written_text,
    )
    return adapter.query(params)


@app.get("/g_publication")
def releven_g_publication(
    params: Annotated[QueryParameters[G_publication], Query()],
) -> Page[G_publication]:
    query = load_query("releven_g_publication")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_publication,
    )
    return adapter.query(params)


@app.get("/g_seal")
def releven_g_seal(params: Annotated[QueryParameters[G_seal], Query()]) -> Page[G_seal]:
    query = load_query("releven_g_seal")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_seal,
    )
    return adapter.query(params)


@app.get("/g_seal_collection")
def releven_g_seal_collection(
    params: Annotated[QueryParameters[G_seal_collection], Query()],
) -> Page[G_seal_collection]:
    query = load_query("releven_g_seal_collection")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_seal_collection,
    )
    return adapter.query(params)


@app.get("/g_boulloterion")
def releven_g_boulloterion(
    params: Annotated[QueryParameters[G_boulloterion], Query()],
) -> Page[G_boulloterion]:
    query = load_query("releven_g_boulloterion")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_boulloterion,
    )
    return adapter.query(params)


@app.get("/g_author_group")
def releven_g_author_group(
    params: Annotated[QueryParameters[G_author_group], Query()],
) -> Page[G_author_group]:
    query = load_query("releven_g_author_group")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_author_group,
    )
    return adapter.query(params)


@app.get("/g_passage")
def releven_g_passage(
    params: Annotated[QueryParameters[G_passage], Query()],
) -> Page[G_passage]:
    query = load_query("releven_g_passage")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_passage,
    )
    return adapter.query(params)


@app.get("/g_ethnic_group")
def releven_g_ethnic_group(
    params: Annotated[QueryParameters[G_ethnic_group], Query()],
) -> Page[G_ethnic_group]:
    query = load_query("releven_g_ethnic_group")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_ethnic_group,
    )
    return adapter.query(params)


@app.get("/g_gender")
def releven_g_gender(
    params: Annotated[QueryParameters[G_gender], Query()],
) -> Page[G_gender]:
    query = load_query("releven_g_gender")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_gender,
    )
    return adapter.query(params)


@app.get("/g_social_relationship")
def releven_g_social_relationship(
    params: Annotated[QueryParameters[G_social_relationship], Query()],
) -> Page[G_social_relationship]:
    query = load_query("releven_g_social_relationship")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_social_relationship,
    )
    return adapter.query(params)


@app.get("/g_language")
def releven_g_language(
    params: Annotated[QueryParameters[G_language], Query()],
) -> Page[G_language]:
    query = load_query("releven_g_language")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_language,
    )
    return adapter.query(params)


@app.get("/g_religious_affiliation")
def releven_g_religious_affiliation(
    params: Annotated[QueryParameters[G_religious_affiliation], Query()],
) -> Page[G_religious_affiliation]:
    query = load_query("releven_g_religious_affiliation")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_religious_affiliation,
    )
    return adapter.query(params)


@app.get("/g_legal_status")
def releven_g_legal_status(
    params: Annotated[QueryParameters[G_legal_status], Query()],
) -> Page[G_legal_status]:
    query = load_query("releven_g_legal_status")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_legal_status,
    )
    return adapter.query(params)


@app.get("/g_social_role")
def releven_g_social_role(
    params: Annotated[QueryParameters[G_social_role], Query()],
) -> Page[G_social_role]:
    query = load_query("releven_g_social_role")
    adapter = SPARQLModelAdapter(
        target="https://wisski-graphdb.acdh-dev.oeaw.ac.at/repositories/blank",
        query=query,
        model=G_social_role,
    )
    return adapter.query(params)


@app.get("/counts")
def counts():
    return {
        "releven_g_external_authority": releven_g_external_authority(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_person": releven_g_person(params=QueryParameters(size=1)).total,
        "releven_g_bibliography": releven_g_bibliography(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_written_text": releven_g_written_text(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_publication": releven_g_publication(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_seal": releven_g_seal(params=QueryParameters(size=1)).total,
        "releven_g_seal_collection": releven_g_seal_collection(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_boulloterion": releven_g_boulloterion(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_author_group": releven_g_author_group(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_passage": releven_g_passage(params=QueryParameters(size=1)).total,
        "releven_g_ethnic_group": releven_g_ethnic_group(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_gender": releven_g_gender(params=QueryParameters(size=1)).total,
        "releven_g_social_relationship": releven_g_social_relationship(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_language": releven_g_language(params=QueryParameters(size=1)).total,
        "releven_g_religious_affiliation": releven_g_religious_affiliation(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_legal_status": releven_g_legal_status(
            params=QueryParameters(size=1)
        ).total,
        "releven_g_social_role": releven_g_social_role(
            params=QueryParameters(size=1)
        ).total,
    }
