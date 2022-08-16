# Function and 'for' Loop Example
# Clean Strings
from pprint import pprint # for easier readability

def clean_string(city):
    return city.replace('%_city%','')

cities = ['%_city%Hamburg',
          '%_city%Munich',
          '%_city%Dresden',
          '%_city%Berlin',
          '%_city%Hannover',
          '%_city%Cologne',
          '%_city%Bonn',
          '%_city%Stuttgart']

for i in range(len(cities)):
    cities[i] = clean_string(cities[i])

pprint(cities)