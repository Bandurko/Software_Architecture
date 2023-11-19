from Products.game_item import GameItem


# Создаем класс продукта (Diamond), являющегося наследником GameItem
class Diamond(GameItem):
    def open(self):
        print('Diamond')