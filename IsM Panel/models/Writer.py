import json


def request(cmd):
    requestadmins = []
    with open('request.json') as f:
        data = json.load(f)

    for item in data:
        requestadmins.append(item)

    requestadmins.append(cmd)

    with open('request.json', 'w') as json_file:
        json.dump(requestadmins, json_file)




