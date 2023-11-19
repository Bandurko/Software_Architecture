from abc import  ABC, abstractmethod


# Создаем прототип (класс) фабрики продуктов (призов) с абстрактным методом create_item
class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass