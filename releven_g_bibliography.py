from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_bibliography(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_bibliography")]

    p_bibliography_item_in_bibliography: Annotated[list[AnyUrl], SPARQLBinding("G_bibliography_g_publication")]
