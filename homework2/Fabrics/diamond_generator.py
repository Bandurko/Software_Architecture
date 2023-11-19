from Fabrics.item_fabrics import ItemFabric
from Products.diamond import Diamond


# Создаем класс (фабрику Diamond), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class DiamondGenerator(ItemFabric):
    def create_item(self):
        return Diamond()