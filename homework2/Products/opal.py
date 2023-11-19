from Products.game_item import GameItem


# Создаем класс продукта (Opal), являющегося наследником GameItem
class Opal(GameItem):
    def open(self):
        print('Opal')