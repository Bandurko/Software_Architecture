from Products.game_item import GameItem


# Создаем класс продукта (Gem), являющегося наследником GameItem
class Gem(GameItem):
    def open(self):
        print('Gem')