#!/bin/bash

# uv sync --upgrade

# remove semantic g_/p_ prefixes for nicer automatically generate class and endpoint names
sed -e 's/id>[gp]_/id>/g' "pathbuilder_20250410_expanded.xml" > tmp.xml

uv run wisskas -v tmp.xml endpoints --git \
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
  -li external_authority '*' \
  -li person 'person_display_name' 'person_id_assignment.**' \
  -ii person/detail id 'person_display_name' 'person_id_assignment.**' '*' \
  -li bibliography '*' \
  -li written_text '*' \
  -li publication '*' \
  -li seal '*' \
  -li seal_collection '*' \
  -li boulloterion '*' \
  -li author_group '*' \
  -li passage '*' \
  -li ethnic_group '*' \
  -li gender '*' \
  -li social_relationship '*' \
  -li language '*' \
  -li religious_affiliation '*' \
  -li legal_status '*' \
  -li social_role '*' \
  -o releven || exit 1
