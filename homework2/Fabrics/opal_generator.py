from Fabrics.item_fabrics import ItemFabric
from Products.opal import Opal


# Создаем класс (фабрику Opal), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class OpalGenerator(ItemFabric):
    def create_item(self):
        return Opal()