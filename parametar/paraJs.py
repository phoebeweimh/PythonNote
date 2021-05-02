import json


def readjs():
    return json.load(open('loginshuju.json', 'r'))['item']


print(readjs())
