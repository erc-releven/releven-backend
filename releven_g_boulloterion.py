from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_boulloterion(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_boulloterion")]

    p_boulloterion_display_name: Annotated[str, SPARQLBinding("G_boulloterion_p_boulloterion_display_name")]
    g_boulloterion_id_assignment: Annotated[list[AnyUrl], SPARQLBinding("G_boulloterion_g_boulloterion_id_assignment")]
    g_boulloterion_produced_seal_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_boulloterion_g_boulloterion_produced_seal_assertion")]
    g_boulloterion_design_element_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_boulloterion_g_boulloterion_design_element_assertion")]
    g_boulloterion_ownership: Annotated[AnyUrl, SPARQLBinding("G_boulloterion_g_boulloterion_ownership")]
