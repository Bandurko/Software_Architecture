from Products.game_item import GameItem


# Создаем класс продукта (Platinum), являющегося наследником GameItem
class Platinum(GameItem):
    def open(self):
        print('Platinum')