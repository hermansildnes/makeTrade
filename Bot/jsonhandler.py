import json


def handlejson():
    variable = open("variables.json",)
    var = json.load(variable)
    return var["variables"][0]


def createjson(json):
    pass
