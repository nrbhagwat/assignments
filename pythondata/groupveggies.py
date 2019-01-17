import csv
import json

#read vegetables.csv into a variable called vegetables
with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader]

#Group by color as a variable vegetables_by_color
vegetables_by_color = {}
for vegetable in vegetables:
	color = vegetable['color']
	if color in vegetables_by_color:
		vegetables_by_color[color].append(vegetable)
	else:
		vegetables_by_color[color] = [vegetable]

#Output vegetables_by_color into a JSON
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent=2)

#Called vegetables_by_color.json