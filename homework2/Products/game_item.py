from abc import  ABC, abstractmethod


# Создаем прототип (класс) продукта (награды) с абстрактным методом open
class GameItem(ABC):
    @abstractmethod
    def open(self):
        pass



