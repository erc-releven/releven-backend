from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_seal(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_seal")]

    p_seal_seal_id: Annotated[str, SPARQLBinding("G_seal_p_seal_seal_id")]
    g_seal_locative_status: Annotated[
        list[AnyUrl], SPARQLBinding("G_seal_g_seal_locative_status")
    ] = None
