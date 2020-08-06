import ccxt
import preload
import apihandler

APIKEY = "zSVrdLDnQeoexXYAF4ybrf1cG8dznNV7V2yQ0AfiWpNdwL50yBGXjdA40EdR1Z73"
SECRETKEY = "sFSSiCycsu9NPP6tKW2bhIcnP71VuPb7p4rP6W5Vmr7lyX3J6WhUNEGJhYPU6pqV"
TIMEOUT = 3000

exchange = preload.initiate("binance", APIKEY, SECRETKEY, TIMEOUT)
markets = preload.loadMarkets(exchange)

SYMBOL = "BTC/USDT"

DIP_THRESHOLD = -1.00
UPWARDS_TREND_THRESHOLD = 1.5

PROFIT_THRESHOLD = 1.25
STOP_LOSS_THRESHOLD = -2.00

PERCENT_TO_TRADE = 50

nextIsBuy = True
lastOpPrice = 11744.89


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
