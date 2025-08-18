#!/bin/bash

# uv sync --upgrade

# remove semantic g_/p_ prefixes for nicer automatically generate class and endpoint names
sed -e 's/id>[gp]_/id>/g' "pathbuilder_wisski.xml" > tmp.xml

uv run wisskas tmp.xml endpoints --git \
  -a "https://graphdb.r11.eu/repositories/RELEVEN_2025" \
  -p aaao "https://ontology.swissartresearch.net/aaao/" \
  -p crm "http://www.cidoc-crm.org/cidoc-crm/" \
  -p lrmoo "http://iflastandards.info/ns/lrm/lrmoo/" \
  -p rdfschema "http://www.w3.org/2000/01/rdf-schema#" \
  -p star "https://r11.eu/ns/star/" \
  -p skos "http://www.w3.org/2004/02/skos/core#" \
  -p r11 "https://r11.eu/ns/spec/" \
  -p r11pros "https://r11.eu/ns/prosopography/" \
  -c -0 \
  -li author_group '*' \
  -li bibliography '*' \
  -li boulloterion '*' \
  -li ethnic_group '*' \
  -li external_authority '*' \
  -li gender '*' \
  -li language '*' \
  -li legal_status '*' \
  -li passage '*' \
  -li person/people\|person_display_name 'person_display_name' 'person_id_assignment.*' 'person_id_assignment.person_id_assignment_identifier.*' 'person_id_assignment.person_id_assignment_by.external_authority_display_name' 'person_name_of_person_assertion.person_name_of_person_is' \
  -ii person/people/detail id 'person_display_name' '*' 'person_gender_assignment.person_gender_assignment_gender_assertion.person_gender_assignment_gender_is.gender_display_name' 'person_id_assignment.*' 'person_id_assignment.person_id_assignment_identifier.*' 'person_name_of_person_assertion.*' 'person_name_of_person_assertion.person_name_of_person_by.*' 'person_name_of_person_assertion.person_name_of_person_src.*' \
  -li place '*' \
  -li publication '*' \
  -li religious_affiliation '*' \
  -li seal '*' \
  -li seal_collection '*' \
  -li social_relationship '*' \
  -li written_text/text\|written_text_display_name '*' 'written_text_creation.*' \
  -ii written_text/text/detail id '*' 'written_text_creation.*' 'written_text_creation.written_text_creation_author_assertion.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_is.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_by.*' 'written_text_creation.written_text_creation_author_assertion.written_text_creation_author_src.*' \
  -o releven || exit 1

for PATCHFILE in `ls *.patch`; do
  patch -p0 < "$PATCHFILE"
done
