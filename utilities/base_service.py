from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def remove(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, updated_info):
        pass
