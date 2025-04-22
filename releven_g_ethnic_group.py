from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_ethnic_group(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_ethnic_group")]

    p_ethnic_group_display_name: Annotated[
        str | None, SPARQLBinding("G_ethnic_group_p_ethnic_group_display_name")
    ] = None
