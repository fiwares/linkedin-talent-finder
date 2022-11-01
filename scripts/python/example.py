import json
from linkedin_api import Linkedin

api = Linkedin('julian.bale67@gmail.com', '3@rFs92.ChuiG}Be07')

people = api.search_people(keywords="ruby AND python", limit=20, include_private_profiles=False, network_depths=["F", "S", "O"], offset=50)
print(json.dumps(people))
#person = api.get_profile(public_id=people[0]['urn_id'])
#print(person)
