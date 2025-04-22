from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated


class PersonFull_PersonAppellationAssertion_PersonAppellationSource(BaseModel):
    model_config = ConfigDict(
        title="Source",
        model_bool="id",
    )
    id: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source"
        ),
    ] = Field(default=None, exclude=False)
    source_publication: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source__source_publication"
        ),
    ] = None
    source_seal: Annotated[
        AnyUrl | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source__source_seal"
        ),
    ] = None
    source_reference: Annotated[
        str | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source__source_reference"
        ),
    ] = None
    source_content: Annotated[
        str | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source__source_content"
        ),
    ] = None


class PersonFull_PersonAppellationAssertion(BaseModel):
    model_config = ConfigDict(
        title="Name(s) in the sources",
        model_bool="id",
    )
    id: Annotated[
        AnyUrl | None, SPARQLBinding("Person_full__person_appellation_assertion")
    ] = Field(default=None, exclude=False)
    person_appellation_source: Annotated[
        PersonFull_PersonAppellationAssertion_PersonAppellationSource | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_source"
        ),
    ] = None
    person_appellation_is: Annotated[
        str | None,
        SPARQLBinding(
            "Person_full__person_appellation_assertion__person_appellation_is"
        ),
    ] = None


class PersonFull(BaseModel):
    model_config = ConfigDict(
        title="Person",
        model_bool="id",
        group_by="id",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("Person_full")] = Field(
        default=None, exclude=False
    )
    person_id_assignment: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_id_assignment")
    ]
    person_appellation_assertion: Annotated[
        list[PersonFull_PersonAppellationAssertion],
        SPARQLBinding("Person_full__person_appellation_assertion"),
    ]
    person_gender_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_gender_assertion")
    ]
    person_ethnicity_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_ethnicity_assertion")
    ]
    person_descriptive_name: Annotated[
        list[str], SPARQLBinding("Person_full__person_descriptive_name")
    ]
    person_possession_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_possession_assertion")
    ]
    person_status_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_status_assertion")
    ]
    person_religion_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_religion_assertion")
    ]
    person_occupation_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_occupation_assertion")
    ]
    person_language_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_language_assertion")
    ]
    person_kinship_assertion: Annotated[
        list[AnyUrl], SPARQLBinding("Person_full__person_kinship_assertion")
    ]
    birth_circumstances_claim: Annotated[
        AnyUrl | None, SPARQLBinding("Person_full__birth_circumstances_claim")
    ] = None
    person_death_assertion: Annotated[
        AnyUrl | None, SPARQLBinding("Person_full__person_death_assertion")
    ] = None
