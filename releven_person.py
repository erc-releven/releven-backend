from typing import Annotated

from pydantic import AnyUrl, BaseModel
from rdfproxy import SPARQLBinding


class Person_PersonAppellationAssertion(BaseModel):
    class Config:
        title = "Name(s) in the sources"
        model_bool = "id"

    id: Annotated[
        AnyUrl | None, SPARQLBinding("person__person_appellation_assertion")
    ] = None
    person_appellation_is: Annotated[
        str | None,
        SPARQLBinding("person__person_appellation_assertion__person_appellation_is"),
    ] = None


class Person(BaseModel):
    class Config:
        title = "Person"
        model_bool = "id"
        group_by = "person"

    id: Annotated[AnyUrl | None, SPARQLBinding("person")] = None
    person_appellation_assertion: Annotated[
        list[Person_PersonAppellationAssertion],
        SPARQLBinding("person__person_appellation_assertion"),
    ]
    person_descriptive_name: Annotated[
        list[str], SPARQLBinding("person__person_descriptive_name")
    ]
