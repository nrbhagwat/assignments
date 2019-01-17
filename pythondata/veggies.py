import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#write the vegetable to a CSV file


with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	#Write header
	writer.writerow(['name', 'color'])
	#Write data
  
	 #loop through each vegetable
	for vegetable in vegetables:
		name = vegetable['name']
		color = vegetable['color']
		writer.writerow([name,color])