from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_gender(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_gender")]

    p_gender_display_name: Annotated[
        str | None, SPARQLBinding("G_gender_p_gender_display_name")
    ] = None
