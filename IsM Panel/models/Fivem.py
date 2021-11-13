import requests

def cheakcount(ip):
	r = requests.get('http://' + ip + '/dynamic.json')
	data = r.json()
	return(data["clients"])

def cheakbanner(ip):
	r = requests.get('http://' + ip + '/info.json')
	data = r.json()
	json_data = data['vars']
	return(json_data["banner_detail"])


def cheakbuild(ip):
	r = requests.get('http://' + ip + '/info.json')
	data = r.json()
	json_data = data['vars']
	return(json_data["sv_enforceGameBuild"])


