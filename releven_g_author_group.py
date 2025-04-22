from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_author_group(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_author_group")]

    p_author_group_display_name: Annotated[
        str, SPARQLBinding("G_author_group_p_author_group_display_name")
    ]
    g_author_group_member_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("G_author_group_g_author_group_member_assertion")
    ] = None
