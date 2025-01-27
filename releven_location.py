from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class Location_Location(BaseModel):
    model_config = ConfigDict(
        title="Location",
        model_bool="id",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("location__location")] = Field(
        default=None, exclude=False
    )
    location_descriptive_name: Annotated[
        str | None, SPARQLBinding("location__location__location_descriptive_name")
    ] = None
