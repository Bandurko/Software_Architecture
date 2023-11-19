from Fabrics.item_fabrics import ItemFabric
from Products.silver import Silver


# Создаем класс (фабрику Silver), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()