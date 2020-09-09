import csv 
import os

def create_csv(category):
	images_list = os.listdir(category)
	columns = ['Filename', 'Category']
	mode = 'w'
	add_header = True
	if(os.path.isfile('train.csv')):
		mode = 'a'
		add_header = False
	with open('train.csv', mode, newline='') as file:
		csv_writer = csv.writer(file)
		if(add_header):
			csv_writer.writerow(columns)
		for id in images_list:
			data = [id, category]
			csv_writer.writerow(data)

categories = ["Adults", "Teenagers", "Toddler"]
for category in categories:
	create_csv(category)