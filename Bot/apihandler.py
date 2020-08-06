import ccxt


def getBalance(exchange):
    return exchange.fetchBalance()["free"]


def getMarketPrice(exchange):
    orderbook = exchange.fetch_order_book(
        exchange.symbols[exchange.symbols.index("BTC/USDT")]
    )
    bid = orderbook["bids"][0][0] if len(orderbook["bids"]) > 0 else None
    ask = orderbook["asks"][0][0] if len(orderbook["asks"]) > 0 else None

    return ask, bid


def placeBuyOrder(exchange, symbol, amount):
    return exchange.createMarketBuyOrder(symbol, amount)


def placeSellOrder(exchange, symbol, amount):
    return exchange.createMarketSellOrder(symbol, amount)
