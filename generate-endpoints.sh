#!/bin/bash

# uv sync --upgrade

# remove semantic g_/p_ prefixes for nicer automatically generate class and endpoint names
sed -e 's/id>[gp]_/id>/g' "pathbuilder_expanded_20251216.xml" > tmp.xml

uv run wisskas tmp.xml endpoints --git \
  -f \
  -a "https://releven-graphdb.acdh-dev.oeaw.ac.at/repositories/owl-max" \
  -p aaao "https://ontology.swissartresearch.net/aaao/" \
  -p crm "http://www.cidoc-crm.org/cidoc-crm/" \
  -p lrmoo "http://iflastandards.info/ns/lrm/lrmoo/" \
  -p owl "http://www.w3.org/2002/07/owl#" \
  -p rdfschema "http://www.w3.org/2000/01/rdf-schema#" \
  -p star "https://r11.eu/ns/star/" \
  -p skos "http://www.w3.org/2004/02/skos/core#" \
  -p r11 "https://r11.eu/ns/spec/" \
  -p r11pros "https://r11.eu/ns/prosopography/" \
  -c -0 \
  -t 60 \
  -r 10 \
  -ll \
  -li author_group '%%' \
  -li authority_status '%%' \
  -li authority_status_type '%%' \
  -li bibliography '%%' \
  -li boulloterion '*' \
  -li correspondence '%%' \
  -li design '%%' \
  -li ethnic_group '%%' \
  -li external_authority '%%' \
  -li gender '%%' \
  -li geopolitical_event_type '%%' \
  -li group '%%' \
  -li manifest_group '%%' \
  -li material '%%' \
  -li language '%%' \
  -li legal_status '%%' \
  -li manuscript '%%' \
  -li manuscript_type '%%' \
  -li passage '%%' \
  -li place_type '%%' \
  -li population '%%' \
  -li publication '%%' \
  -li object_type '%%' \
  -li religious_affiliation '%%' \
  -li social_relationship '%%' \
  -li social_relation_category '%%' \
  -li social_quality '%%' \
  -li work '%%' \
  \
  \
   -li person/people\|person_display_name 'person_display_name' 'person_id_assignment.*' 'person_id_assignment.person_id_assignment_identifier.*' 'person_id_assignment.person_id_assignment_by.external_authority_display_name' 'person_name_of_person_assertion.person_name_of_person_is' 'person_gender_assignment#' 'person_ethnic_group_membership_assertion#' 'person_population_membership_assertion#' 'part_of_manifest_group_assertion#' 'person_social_relationship#' 'person_language_skill#' 'person_social_role#' 'person_legal_role#' 'person_religious_affiliation#' 'person_possession_assertion#' 'person_same_as_person_assertion#' \
  -ii person/people/detail id 'person_display_name' 'person_id_assignment.*.*' \
  -ii person/people/identity id 'person_name_of_person_assertion.*.*' 'person_ethnic_group_membership_assertion.*.*' 'person_population_membership_assertion.*.*' 'person_part_of_manifest_group_assertion.*.*' 'person_possession_assertion.*.*' \
  -ii person/people/life_events id 'person_gender_assignment.*.*.*' 'person_birth_of_person.*.*' 'person_death_of_person.*.*' 'person_language_skill.*.*' 'person_religious_affiliation.*.*' \
  -ii person/people/cursus id 'person_legal_role.*.*' 'person_social_role.*.*' \
  \
  -li geopolitical_event\|geopolitical_event_display_name '*' \
  -li journey '*' \
  \
  -li place/places\|place_display_name 'place_display_name' 'place_id_assignment.*' 'place_id_assignment.place_id_assignment_identifier.place_id_assignment_identifier_plain' 'place_id_assignment.place_id_assignment_by.*' 'place_corresponds_to_assertion#' 'place_name_of_place_assertion#' 'place_part_of_place_assertion#' 'place_type_of_place_assertion#' 'place_spatiotemporal_existence.place_spatiotemporal_existence_time_frame_assertion#' 'place_spatiotemporal_existence.place_spatiotemporal_existence_location_assertion#' 'place_succeeded_by_assertion#' 'place_had_population_assertion#' 'place_same_as_place_assertion#' \
  -ii place/places/detail id '%%' \
  \
  -li seal/seals 'seal_seal_id' 'seal_locative_status.seal_locative_status_location_assertion#' 'seal_locative_status.seal_locative_status_time_frame_assertion#' \
  -ii seal/seals/detail id '%%' \
  -li seal_collection '*' \
  \
  -li written_text/texts\|written_text_display_name 'written_text_display_name' 'written_text_title_assertion#' 'written_text_creation.written_text_creation_time_frame_assertion#' 'written_text_creation.written_text_creation_author_assertion#' 'written_text_creation.written_text_creation_place_assertion#' 'written_text_creation.written_text_creation_copied_from_assertion#' 'written_text_creation.written_text_creation_translated_from_assertion#' 'written_text_published_as_assertion#' 'written_text_written_in_assertion#' 'written_text_version_of_assertion#' 'written_text_used_as_source_assertion#' 'written_text_same_as_text_assertion#' \
  -ii written_text/texts/detail id '*' 'written_text_creation.*' 'written_text_creation.written_text_creation_author_assertion.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_is.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_by.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_src.*' \
  -o releven || exit 1

for PATCHFILE in `ls *.patch`; do
  patch -p0 < "$PATCHFILE"
done
