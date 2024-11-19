from typing import Annotated

from pydantic import AnyUrl, BaseModel
from rdfproxy import SPARQLBinding


class WrittenWork_WorkCreationAssertion_WorkCreation(BaseModel):
    class Config:
        title = "text_creation"
        model_bool = "id"
        group_by = "written_work__work_creation_assertion__work_creation"

    id: Annotated[
        AnyUrl | None,
        SPARQLBinding("written_work__work_creation_assertion__work_creation"),
    ] = None
    work_creation_6464e7f7408f5: Annotated[
        list[AnyUrl],
        SPARQLBinding(
            "written_work__work_creation_assertion__work_creation__work_creation_6464e7f7408f5"
        ),
    ]
    text_creation_timeframe_assertio: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "written_work__work_creation_assertion__work_creation__text_creation_timeframe_assertio"
        ),
    ] = None


class WrittenWork_WorkCreationAssertion(BaseModel):
    class Config:
        title = "text_creation_assertion"
        model_bool = "id"

    id: Annotated[
        AnyUrl | None, SPARQLBinding("written_work__work_creation_assertion")
    ] = None
    work_creation: Annotated[
        WrittenWork_WorkCreationAssertion_WorkCreation | None,
        SPARQLBinding("written_work__work_creation_assertion__work_creation"),
    ] = None
    work_creation_assertion_by: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "written_work__work_creation_assertion__work_creation_assertion_by"
        ),
    ] = None
    work_creation_assertion_by_64676da87229e: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "written_work__work_creation_assertion__work_creation_assertion_by_64676da87229e"
        ),
    ] = None


class WrittenWork(BaseModel):
    class Config:
        title = "Text Expression"
        model_bool = "id"
        group_by = "written_work"

    id: Annotated[AnyUrl | None, SPARQLBinding("written_work")] = None
    written_work_label: Annotated[
        str | None, SPARQLBinding("written_work__written_work_label")
    ] = None
    work_creation_assertion: Annotated[
        list[WrittenWork_WorkCreationAssertion],
        SPARQLBinding("written_work__work_creation_assertion"),
    ]
