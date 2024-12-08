from typing import Annotated

from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding


class Location(BaseModel):
    model_config = ConfigDict(
        title="Location",
        model_bool="id",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("location")] = Field(
        default=None, exclude=True
    )
    location_descriptive_name: Annotated[
        str | None, SPARQLBinding("location__location_descriptive_name")
    ] = None
