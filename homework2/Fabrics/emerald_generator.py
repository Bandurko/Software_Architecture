from Fabrics.item_fabrics import ItemFabric
from Products.emerald import Emerald


# Создаем класс (фабрику Emerald), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class EmeraldGenerator(ItemFabric):
    def create_item(self):
        return Emerald()