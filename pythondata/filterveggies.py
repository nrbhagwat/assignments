#Ruha and Nikhil
#Read vegetables.csv into a variable called vegetables.
import csv
import json

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

#Loop through vegetables and filter down to only green vegtables using a whitelist.
	greenveggies = []
	whitelist = ['green']
	for vegetable in vegetables:
		if vegetable['color'] in whitelist:
			greenveggies.append(vegetable)

#Print veggies to the terminal
print(greenveggies)

#Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as f:
    json.dump(greenveggies, f, indent=2)