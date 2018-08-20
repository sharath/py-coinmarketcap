from enum import Enum
import requests
import threading
from bs4 import BeautifulSoup

from ..token import Token

AllKeysPage = 'https://coinmarketcap.com/all/views/all/'


class Worker:
    def __init__(self, api_key: str = None) -> None:
        self.api_key = api_key

    def fetch_all(self) -> list:
        return self.__api_fetch_all() if self.api_key else self.__bs4_fetch_all()

    def __bs4_fetch_all(self) -> list:
        global AllKeysPage
        resp = requests.get(AllKeysPage)
        soup = BeautifulSoup(resp.content, 'html.parser')
        tokens = []
        for raw in soup.select('tr')[1:]:
            symbol, name, price_usd, price_btc, hchange, dchange, wchange = '', '', -1, -1, -1, -1, -1
            try:
                symbol = raw.select('.col-symbol')[0].contents[0]
                name = raw.select('.currency-name-container')[0].contents[0]
                price_usd = float(raw.select('.price')[0].attrs['data-usd'])
                price_btc = float(raw.select('.price')[0].attrs['data-btc'])
                hchange, dchange, wchange = [v.attrs['data-percentusd'] for v in raw.select('.percent-change')]
            except:
                pass
            tokens.append(Token(symbol, name, price_usd, price_btc, hchange, dchange, wchange))
        return tokens

    def __api_fetch_all(self) -> list:
        pass


class WorkerCircularQueue:
    def __init__(self) -> None:
        self.__lock = threading.Lock()
        self.__workers = []

    def add(self, worker: Worker) -> None:
        with self.__lock:
            self.__enqueue(worker)

    def next(self) -> Worker:
        with self.__lock:
            t = self.__dequeue()
            self.__enqueue(t)
            return t

    def __enqueue(self, worker: Worker) -> None:
        self.__workers.append(worker)

    def __dequeue(self) -> Worker:
        return self.__workers.pop(0)

    def __len__(self) -> int:
        return len(self.__workers)
