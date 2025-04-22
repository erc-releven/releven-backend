from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_legal_status(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_legal_status")]

    p_legal_status_display_name: Annotated[str | None, SPARQLBinding("G_legal_status_p_legal_status_display_name")] = None
