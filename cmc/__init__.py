import torch
from enum import Enum


class Methods(Enum):
    bs4 = "bs4"
    api = "api"


class Worker:
    def __init__(self, method: Methods = Methods.bs4, apikeys: list = None) -> None:
        self.method = method
        self.apikeys = apikeys


class WorkerCircularQueue:
    def __init__(self) -> None:
        self.__workers = []

    def add(self, worker: Worker) -> None:
        self.__enqueue(worker)

    def next(self) -> Worker:
        t = self.__dequeue()
        self.__enqueue(t)
        return t

    def __enqueue(self, worker: Worker) -> None:
        self.__workers.append(worker)

    def __dequeue(self) -> Worker:
        return self.__workers.pop(0)

    def __len__(self) -> int:
        return len(self.__workers)
