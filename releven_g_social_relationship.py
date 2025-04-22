from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_social_relationship(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_social_relationship")]

    p_social_relationship_display_name: Annotated[
        str, SPARQLBinding("G_social_relationship_p_social_relationship_display_name")
    ]
    g_social_relationship_categorisation_assertion: Annotated[
        list[AnyUrl],
        SPARQLBinding(
            "G_social_relationship_g_social_relationship_categorisation_assertion"
        ),
    ] = None
