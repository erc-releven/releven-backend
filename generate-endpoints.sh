#!/bin/bash

# remove semantic g_/p_ prefixes for nicer automatically generate class and endpoint names
sed -e 's/id>[gp]_/id>/g' "pathbuilder_20250410_expanded.xml" > tmp.xml

uv run wisskas -vvv tmp.xml endpoints --git \
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
  -ei external_authority '*' \
  -ei person '*' 'person_id_assignment.*' \
  -ei bibliography '*' \
  -ei written_text '*' \
  -ei publication '*' \
  -ei seal '*' \
  -ei seal_collection '*' \
  -ei boulloterion '*' \
  -ei author_group '*' \
  -ei passage '*' \
  -ei ethnic_group '*' \
  -ei gender '*' \
  -ei social_relationship '*' \
  -ei language '*' \
  -ei religious_affiliation '*' \
  -ei legal_status '*' \
  -ei social_role '*' \
  -o releven || exit 1
