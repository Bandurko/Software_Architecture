from Products.game_item import GameItem


# Создаем класс продукта (Ruby), являющегося наследником GameItem
class Ruby(GameItem):
    def open(self):
        print('Ruby')