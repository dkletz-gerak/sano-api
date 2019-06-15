from types import FunctionType
from abc import ABC, abstractmethod


class Middleware(ABC):
    def __init__(self):
        self.next = None

    def add_next(self, func: FunctionType):
        self.next = func
        return self

    @abstractmethod
    def pre_check(self, *args, **kwargs):
        pass

    @abstractmethod
    def default(self):
        pass

    def __call__(self, *args, **kwargs):
        if self.pre_check(*args, **kwargs):
            return self.next(*args, **kwargs)
        else:
            return self.default()
