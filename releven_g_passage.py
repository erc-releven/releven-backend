from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_passage(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_passage")]

    p_passage_reference_string: Annotated[str, SPARQLBinding("G_passage_p_passage_reference_string")]
    p_passage_content: Annotated[str, SPARQLBinding("G_passage_p_passage_content")]
    g_passage_in_publication_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_passage_g_passage_in_publication_assertion")]
    g_passage_on_object_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_passage_g_passage_on_object_assertion")]
    g_passage_on_boulloterion_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_passage_g_passage_on_boulloterion_assertion")]
