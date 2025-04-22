from pydantic import AnyUrl, BaseModel, Field  # noqa: F401
from rdfproxy import ConfigDict, SPARQLBinding
from typing import Annotated



class GPersonIdAssignment(BaseModel):
    model_config = ConfigDict(
        title="",
    )
    id: Annotated[AnyUrl | None, SPARQLBinding("G_person_g_person_id_assignment")] = None

    g_person_id_assignment_identifier: Annotated[AnyUrl | None, SPARQLBinding("G_person_g_person_id_assignment_g_person_id_assignment_identifier")] = None
    p_person_id_assignment_by: Annotated[AnyUrl | None, SPARQLBinding("G_person_g_person_id_assignment_g_external_authority")] = None



class G_person(BaseModel):
    model_config = ConfigDict(
        title="",
        group_by="id",
    )
    id: Annotated[AnyUrl, SPARQLBinding("G_person")]

    p_person_display_name: Annotated[str, SPARQLBinding("G_person_p_person_display_name")]
    g_person_id_assignment: Annotated[list[GPersonIdAssignment], SPARQLBinding("G_person_g_person_id_assignment")]
    g_person_name_of_person_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_name_of_person_assertion")]
    g_person_birth_of_person: Annotated[AnyUrl, SPARQLBinding("G_person_g_person_birth_of_person")]
    g_person_gender_assignment: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_gender_assignment")]
    g_person_ethnic_group_membership_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_ethnic_group_membership_assertion")]
    g_person_population_membership_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_population_membership_assertion")]
    g_person_part_of_embodiment_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_part_of_embodiment_assertion")]
    g_person_social_relationship: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_social_relationship")]
    g_person_language_skill: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_language_skill")]
    g_person_social_role: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_social_role")]
    g_person_legal_role: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_legal_role")]
    g_person_religious_affiliation: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_religious_affiliation")]
    g_person_possession_assertion: Annotated[list[AnyUrl], SPARQLBinding("G_person_g_person_possession_assertion")]
    g_person_death_of_person: Annotated[AnyUrl, SPARQLBinding("G_person_g_person_death_of_person")]
