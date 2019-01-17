#Simon and Nikhil

#Read superheroes.json
import json
from pprint import pprint

with open('superheroes.json', 'r') as f:
    squad = json.load(f)
    
#Create empty array called powers
allpowers = []

#Loop through members of the squad, append powers of each to the powers array
members = squad['members']
for member in members:
	powers = member['powers']
	for power in powers:
		allpowers.append(power)

#print each power to the terminal

pprint(allpowers)