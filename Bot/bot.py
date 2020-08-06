import ccxt
import jsonhandler
import preload
import apihandler

APIKEY = "zSVrdLDnQeoexXYAF4ybrf1cG8dznNV7V2yQ0AfiWpNdwL50yBGXjdA40EdR1Z73"
SECRETKEY = "sFSSiCycsu9NPP6tKW2bhIcnP71VuPb7p4rP6W5Vmr7lyX3J6WhUNEGJhYPU6pqV"
TIMEOUT = 3000

try:
    variables = jsonhandler.handlejson()

except FileNotFoundError:
    variables = jsonhandler.createjson()

SYMBOL = variables["SYMBOL"]

DIP_THRESHOLD = variables["DIP_THRESHOLD"]
UPWARDS_TREND_THRESHOLD = variables["UPWARDS_TREND_THRESHOLD"]
PROFIT_THRESHOLD = variables["PROFIT_THRESHOLD"]
STOP_LOSS_THRESHOLD = variables["STOP_LOSS_THRESHOLD"]

PERCENT_TO_TRADE = variables["PERCENT_TO_TRADE"]

nextIsBuy = variables["nextIsBuy"]
lastOpPrice = variables["lastOpPrice"]


exchange = preload.initiate("binance", APIKEY, SECRETKEY, TIMEOUT)
markets = preload.loadMarkets(exchange)


def makeTrade():
    marketask, marketbid = apihandler.getMarketPrice(exchange)
    if nextIsBuy:
        currentPrice = marketask
    else:
        currentPrice = marketbid

    diff = (currentPrice - lastOpPrice) / lastOpPrice * 100
    if nextIsBuy:
        tryToBuy(diff)
    else:
        tryToSell(diff)


def tryToBuy(diff):
    if diff >= UPWARDS_TREND_THRESHOLD or diff <= DIP_THRESHOLD:
        balance = apihandler.getBalance(exchange)
        lastOpPrice = apihandler.placeBuyOrder(
            exchange, symbol, (balance / 100) * PERCENT_TO_TRADE
        )
        nextIsBuy = False


def tryToSell(diff):
    if diff >= PROFIT_THRESHOLD or diff <= STOP_LOSS_THRESHOLD:
        balance = apihandler.getBalance(exchange)
        lastOpPrice = apihandler.placeSellOrder(
            exchange, symbol, (balance / 100) * PERCENT_TO_TRADE
        )
        nextIsBuy = True


def main(diff):
    while True:
        makeTrade()
        time.sleep(5)
