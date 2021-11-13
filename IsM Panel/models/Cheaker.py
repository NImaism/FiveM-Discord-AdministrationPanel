import json

with open('config.json') as f:
	data = json.load(f)

json_data = data['Users']



def cheakadmin(user):
	for item in json_data:
		if user in item['Admins']:
			return True

def cheakip(user):
	for item in json_data:
		if user in item['Admins']:
			return item['Ip']

def cheakowner(user):
	for item in json_data:
		if user in item['Admins']:
			return item['Owner']

def cheakapi(user):
	for item in json_data:
		if user in item['Admins']:
			return item['Api']

def cheaklink(user):
	for item in json_data:
		if user in item['Admins']:
			return item['Site']



