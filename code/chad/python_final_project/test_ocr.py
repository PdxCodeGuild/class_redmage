import json

with open('rules.json') as rulefile:
    rules = json.load(rulefile)



print(rules.keys()) # Level 1 is keywords
print(rules['northwes']['l2keywords']) #Level 2 keywords
print(rules['northwes']['l2keywords']['4plex']) # Level 2 Pretty Name
print(rules['prettyname']['type'])