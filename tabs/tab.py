from abc import ABC, abstractmethod


class TabInterface(ABC):

    @abstractmethod
    def render():
        pass
