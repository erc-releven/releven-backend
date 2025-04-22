from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_written_text(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_written_text")]

    p_written_text_display_name: Annotated[
        str, SPARQLBinding("G_written_text_p_written_text_display_name")
    ]
    g_written_text_title_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("G_written_text_g_written_text_title_assertion")
    ] = None
    g_written_text_creation: Annotated[
        AnyUrl, SPARQLBinding("G_written_text_g_written_text_creation")
    ]
    g_written_text_published_as_assertion: Annotated[
        list[AnyUrl],
        SPARQLBinding("G_written_text_g_written_text_published_as_assertion"),
    ] = None
    g_written_text_written_in_assertion: Annotated[
        list[AnyUrl],
        SPARQLBinding("G_written_text_g_written_text_written_in_assertion"),
    ] = None
    g_written_text_version_of_assertion: Annotated[
        list[AnyUrl],
        SPARQLBinding("G_written_text_g_written_text_version_of_assertion"),
    ] = None
