import requests
import json
import pprint
import pdb

printer = pprint.PrettyPrinter(indent=4).pprint

print("hi")
r = requests.get("https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches1.json")

assert r.status_code in (200, 400), "Status code must be either 200 or 400"

print("hey")
top_level_dict = json.loads(r.text)

unique_keys = set()

for match in top_level_dict['matches']:
    for object_key in match:
        unique_keys.add(object_key)

printer(unique_keys)

print(top_level_dict['matches'][0]['teams'])
print("hi")
pdb.set_trace()
