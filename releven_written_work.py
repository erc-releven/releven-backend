from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class WrittenWork_WrittenWork(BaseModel):
    model_config = ConfigDict(
        title="Text Expression",
        model_bool="id",
        group_by="id",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("written_work__written_work")] = Field(
        default=None, exclude=False
    )
    written_work_label: Annotated[
        str | None, SPARQLBinding("written_work__written_work__written_work_label")
    ] = None
    work_creation_assertion: Annotated[
        list[AnyUrl],
        SPARQLBinding("written_work__written_work__work_creation_assertion"),
    ]
