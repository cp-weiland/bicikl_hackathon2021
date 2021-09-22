import sys, os, re, json
import codecs

from SPARQLWrapper import SPARQLWrapper, JSON
#from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://dissco-mf.bgbm.org:8282/proxy/wdqs/bigdata/namespace/wdq/sparql")
#sparql = SPARQLWrapper("http://semantics.senckenberg.de/sparql")

sparql.setQuery("""
PREFIX wd: <http://wikibase.svc/entity/>
PREFIX wdt: <http://wikibase.svc/prop/direct/>

SELECT ?section ?sectionLabel ?item ?itemLabel ?itemDescription ?example ?dataType ?min ?max WHERE {
  #the type to export is ODStype1802
  BIND(wd:Q41 as $type).
  
  {
    #get all of the statements that are not sections
    ?type p:P44 ?statement.
    ?statement ps:P44 ?item.
    ?statement pqv:P45/wikibase:quantityAmount ?order.
    MINUS {?item wdt:P1 wd:Q39}.
  }UNION{
    #get all of the sections
    ?type p:P44 ?statement.
    ?statement ps:P44 ?section.
    ?statement pqv:P45/wikibase:quantityAmount ?order.
    ?section wdt:P1 wd:Q39.
  
    #get the items of the section
    ?item wdt:P4 ?section.
  }
  #additional optional properties
  OPTIONAL {?item wdt:P18 ?example}
  OPTIONAL {?item wdt:P10 ?dataType}
  OPTIONAL {?item wdt:P37 ?min}
  OPTIONAL {?item wdt:P38 ?max}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  
}ORDER BY ?order
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

with open('data.json', 'w') as outfile:
    json.dump(results, outfile)
