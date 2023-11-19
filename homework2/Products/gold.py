from Products.game_item import GameItem


# Создаем класс продукта (Gold), являющегося наследником GameItem
class Gold(GameItem):
    def open(self):
        print('Gold')