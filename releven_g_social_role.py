from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class G_social_role(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_social_role")]

    p_social_role_display_name: Annotated[str | None, SPARQLBinding("G_social_role_p_social_role_display_name")] = None
