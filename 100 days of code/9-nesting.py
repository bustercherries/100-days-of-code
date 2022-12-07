travel_log = {
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
#🚨 Do NOT change the code above 
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

def add_new_country(country, visits, cities):
    new_dictionary = {}
    new_dictionary["country"] = country
    new_dictionary["visits"] = visits
    new_dictionary["cities"] = cities
    travel_log.append(new_dictionary)

#🚨 Do NOT change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

travel_log[1] = 4
print(travel_log)