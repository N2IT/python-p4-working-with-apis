
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://data.cityofnewyork.us/resource/w7w3-xahh.json"

    response = requests.get(URL)
    return response.content

  def business_industries(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
        programs_list.append(program["industry"])

    return programs_list
  
programs = GetPrograms()
industries = programs.business_industries()

for industry in set(industries):
  print(industry)



# programs = GetPrograms().get_programs()
# print(programs)