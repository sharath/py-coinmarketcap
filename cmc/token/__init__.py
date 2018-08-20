class Token:
    def __init__(self, symbol: str, name: str, price_usd: float, price_btc: float, hchange: float, dchange: float,
                 wchange: float) -> None:
        self.symbol = symbol
        self.name = name
        self.price_usd = price_usd
        self.price_btc = price_btc
        self.hchange = hchange
        self.dchange = dchange
        self.wchange = wchange

    def __str__(self):
        return str(vars(self))
