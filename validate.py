from rdflib import Graph, Namespace
from pyshex.evaluate import evaluate

import json, sys, os, re 

with open("data02.json") as data_foo:
    my_data = data_foo.read()


with open("schema02.shex") as shex_foo:
    shex = shex_foo.read()


ODS = Namespace("http://github.com/hardistyar/openDS/terms/")

g = Graph()
g.parse(data=my_data, format="json-ld")
#print("Graph serialization")
#print(g.serialize(format='n3'))
    
rslt, reason = evaluate(g, shex, "https://doi.org/20.5000.1025/ae88bb3a666ec72dbc52")
print(rslt)
