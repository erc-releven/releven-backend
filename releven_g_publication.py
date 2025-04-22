from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_publication(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_publication")]

    p_publication_display_name: Annotated[str, SPARQLBinding("G_publication_p_publication_display_name")]
    g_publication_creation: Annotated[AnyUrl, SPARQLBinding("G_publication_g_publication_creation")]
    g_publication_derived_from_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_publication_g_publication_derived_from_assertion")]
