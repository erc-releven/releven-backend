from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class G_language(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_language")]

    p_language_display_name: Annotated[
        str | None, SPARQLBinding("G_language_p_language_display_name")
    ] = None
