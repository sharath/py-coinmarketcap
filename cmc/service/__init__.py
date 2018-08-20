import time
import threading

from ..token import Token

from ..worker import WorkerCircularQueue, Worker


class CMCService:
    def __init__(self, update_interval: float = 15, apikeys=None, start=True) -> None:
        self.__lock = threading.Lock()
        self.__cache = {}
        self.__q = WorkerCircularQueue()
        self.__kill = False
        if apikeys:
            for k in apikeys:
                self.__q.add(Worker(k))
        else:
            self.__q.add(Worker())
        self.__update()
        if start:
            self.start_service(update_interval)

    def __update(self):
        worker = self.__q.next()
        tokens = worker.fetch_all()
        with self.__lock:
            for token in tokens:
                self.__cache[token.name] = token

    def __update_service(self, update_interval: float = 15) -> None:
        start = time.time()
        while True:
            if self.__kill:
                return
            if time.time() - start > update_interval:
                start - time.time()
                self.__update()

    def fetch_token(self, name: str) -> Token:
        with self.__lock:
            return self.__cache[name]

    def kill_service(self):
        self.__kill = True

    def start_service(self, update_interval: float = 15):
        self.__kill = False
        threading.Thread(target=self.__update_service, kwargs={'update_interval': update_interval}).start()
