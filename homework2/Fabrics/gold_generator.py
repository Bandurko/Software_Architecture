from Fabrics.item_fabrics import ItemFabric
from Products.gold import Gold


# Создаем класс (фабрику Gold), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()
