import ccxt
from termcolor import colored


def initiate(exchange_name, APIKEY, SECRETKEY, TIMEOUT):
    print(f"\nConnecting to {exchange_name}...")

    exchange_id = exchange_name
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class(
        {
            "apiKey": APIKEY,
            "secret": SECRETKEY,
            "timeout": TIMEOUT,
            "enableRateLimit": True,
        }
    )

    print(
        "Successfully connected to "
        + colored(f"{exchange_name}", "green")
        + "!\n"
    )
    return exchange


def loadMarkets(exchange):
    print("Loading markets...")

    markets = exchange.load_markets()

    print(f"Successfully loaded markets!\n")
    return markets
