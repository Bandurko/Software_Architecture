from Fabrics.item_fabrics import ItemFabric
from Products.platinum import Platinum


# Создаем класс (фабрику Platinum), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Platinum()