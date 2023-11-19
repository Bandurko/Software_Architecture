from Products.game_item import GameItem


# Создаем класс продукта (Emerald), являющегося наследником GameItem
class Emerald(GameItem):
    def open(self):
        print('Emerald')