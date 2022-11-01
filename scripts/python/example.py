from linkedin_api import Linkedin

api = Linkedin('julian.bale67@gmail.com', '3@rFs92.ChuiG}Be07')

people = api.search_people(keywords="ruby AND python AND java", limit=5)
person = api.get_profile(public_id=people[0]['urn_id'])
print(person)
