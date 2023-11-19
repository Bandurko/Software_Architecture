from Products.game_item import GameItem


# Создаем класс продукта (Silver), являющегося наследником GameItem
class Silver(GameItem):
    def open(self):
        print('Silver')