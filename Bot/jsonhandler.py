import json


def loadjson():
    varfile = open("variables.json",)
    variable = json.load(varfile)
    var = variable["variables"][0]
    return var, varfile


def createjson():
    data = {}
    data["variables"] = []
    data["variables"].append(
        {
            "SYMBOL": "BTC/USDT",
            "DIP_THRESHOLD": -1.00,
            "UPWARDS_TREND_THRESHOLD": 1.5,
            "PROFIT_THRESHOLD": 1.25,
            "STOP_LOSS_THRESHOLD": -2.00,
            "PERCENT_TO_TRADE": 50,
            "nextIsBuy": True,
            "lastOpPrice": 11744.89,
        }
    )
    varfile = open("variables.json", "w")
    json.dump(data, varfile)
    varfile.close()

    varfile = open("variables.json",)
    variable = json.load(varfile)
    var = variable["variables"][0]
    return var, varfile


def updatejson(variable, nextIsBuy, lastOpPrice):
    variable["nextIsBuy"] = nextIsBuy
    variable["lastOpPrice"] = lastOpPrice
    varfile = open("variables.json", "w")
    json.dump(variable, varfile)
