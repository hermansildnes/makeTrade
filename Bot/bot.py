import ccxt
import time
import jsonhandler
import preload
import apihandler

# Sets APIKEY, SECRETKEY and TIMEOUT, then uses it to initiate
# exchange and load markets
APIKEY = ""
SECRETKEY = ""
TIMEOUT = 3000

exchange = preload.initiate("binance", APIKEY, SECRETKEY, TIMEOUT)
markets = preload.loadMarkets(exchange)

# Tries to load json-file containing variables for trading.
# If the file doesnt exsist: Creates one.
try:
    variables, varfile = jsonhandler.loadjson()

except FileNotFoundError:
    variables, varfile = jsonhandler.createjson()

SYMBOL = variables["SYMBOL"]

DIP_THRESHOLD = variables["DIP_THRESHOLD"]
UPWARDS_TREND_THRESHOLD = variables["UPWARDS_TREND_THRESHOLD"]
PROFIT_THRESHOLD = variables["PROFIT_THRESHOLD"]
STOP_LOSS_THRESHOLD = variables["STOP_LOSS_THRESHOLD"]

PERCENT_TO_TRADE = variables["PERCENT_TO_TRADE"]

nextIsBuy = variables["nextIsBuy"]
lastOpPrice = variables["lastOpPrice"]


def makeTrade():
    marketask, marketbid = apihandler.getMarketPrice(exchange)
    if nextIsBuy:
        currentPrice = marketask
    else:
        currentPrice = marketbid

    diff = (currentPrice - lastOpPrice) / lastOpPrice * 100
    if nextIsBuy:
        if tryToBuy(diff):
            return "Trade successful!"
        else:
            return "Trade failed :("
    else:
        if tryToSell(diff):
            return "Trade successful!"
        else:
            return "Trade failed :("


def tryToBuy(diff):
    if diff >= UPWARDS_TREND_THRESHOLD or diff <= DIP_THRESHOLD:
        balance = apihandler.getBalance(exchange)
        lastOpPrice = apihandler.placeBuyOrder(
            exchange, symbol, (balance / 100) * PERCENT_TO_TRADE
        )
        nextIsBuy = False
        return True
    return False


def tryToSell(diff):
    if diff >= PROFIT_THRESHOLD or diff <= STOP_LOSS_THRESHOLD:
        balance = apihandler.getBalance(exchange)
        lastOpPrice = apihandler.placeSellOrder(
            exchange, symbol, (balance / 100) * PERCENT_TO_TRADE
        )
        nextIsBuy = True
        return True
    return False


def main():
    while True:
        print(makeTrade())
        jsonhandler.updatejson(variables, nextIsBuy, lastOpPrice)
        time.sleep(5)
