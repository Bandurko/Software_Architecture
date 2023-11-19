from Fabrics.item_fabrics import ItemFabric
from Products.gem import Gem


# Создаем класс (фабрику Gem), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()