from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_external_authority(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_external_authority")]

    p_external_authority_display_name: Annotated[str | None, SPARQLBinding("G_external_authority_p_external_authority_display_name")] = None
