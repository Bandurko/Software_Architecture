from Fabrics.item_fabrics import ItemFabric
from Products.ruby import Ruby


# Создаем класс (фабрику Ruby), который является наследником класса ItemFabric и у него
# будет переопределен метод create_item
class RubyGenerator(ItemFabric):
    def create_item(self):
        return Ruby()