from libs.ABC import ABC, abstractmethod


class Scraper(ABC):

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def extract_data(self, data):
        pass

    @abstractmethod
    def save(self, data: dict):
        pass

    @abstractmethod
    def work(self):
        pass
