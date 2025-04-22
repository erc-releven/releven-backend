from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class Locationlocation_Location(BaseModel):
    model_config = ConfigDict(
        title="Location",
        model_bool="id",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("LocationLocation__location")] = Field(
        default=None, exclude=False
    )
    location_descriptive_name: Annotated[
        str | None,
        SPARQLBinding("LocationLocation__location__location_descriptive_name"),
    ] = None
