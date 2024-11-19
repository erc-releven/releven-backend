from typing import Annotated

from pydantic import AnyUrl, BaseModel
from rdfproxy import SPARQLBinding


class Location(BaseModel):
    class Config:
        title = "Location"
        model_bool = "id"

    id: Annotated[AnyUrl | None, SPARQLBinding("location")] = None
    location_descriptive_name: Annotated[
        str | None, SPARQLBinding("location__location_descriptive_name")
    ] = None
