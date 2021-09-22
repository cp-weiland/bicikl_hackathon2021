import sys, os, re, json
import codecs

with open('data.json') as json_file:
     data = json.load(json_file)
     
my_results = data["results"]["bindings"]
#elem = my_results.keys()

protoshex = {}

for i in my_results:
     keys = i.keys()
     if "section" in i.keys():
          print(i["sectionLabel"]["value"])
#          for elem in i.keys():
#               print(elem, i[elem])
     else:
          print("main")
     
