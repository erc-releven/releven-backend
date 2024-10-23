from pydantic import BaseModel, AnyUrl
from rdfproxy import SPARQLBinding
from typing import Annotated

class Person(BaseModel):
    class Config:
        title = "Person"
        original_path_id = "person"
        group_by = "person"
    id: Annotated[AnyUrl, SPARQLBinding("person")]
    person_descriptive_name: Annotated[list[str], SPARQLBinding("person__person_descriptive_name")]


