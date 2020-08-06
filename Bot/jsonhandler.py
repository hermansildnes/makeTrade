import json


def handlejson():
    variable = open("variables.json",)
    var = json.load(variable)
    return var["variables"][0]


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
            "nextIsBuy": true,
            "lastOpPrice": 11744.89,
        }
    )
    variables = open("variables.json", "w")
    json.dump(data, variables)
    variables.close()

    variable = open("variables.json",)
    var = json.load(variable)
    return var["variables"][0]
