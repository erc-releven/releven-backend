from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_seal_collection(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_seal_collection")]

    p_seal_collection_display_name: Annotated[str, SPARQLBinding("G_seal_collection_p_seal_collection_display_name")]
    g_seal_collection_seal_in_collection_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_seal_collection_g_seal_collection_seal_in_collection_assertion")]
    g_seal_collection_ownership_change: Annotated[list[AnyUrl], SPARQLBinding("G_seal_collection_g_seal_collection_ownership_change")]
