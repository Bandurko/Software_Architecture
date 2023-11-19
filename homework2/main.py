from random import randint

from Fabrics.diamond_generator import DiamondGenerator
from Fabrics.emerald_generator import EmeraldGenerator
from Fabrics.gem_generator import GemGenerator
from Fabrics.gold_generator import GoldGenerator
from Fabrics.opal_generator import OpalGenerator
from Fabrics.platinum_generator import PlatinumGenerator
from Fabrics.ruby_generator import RubyGenerator
from Fabrics.silver_generator import SilverGenerator

if __name__=='__main__':
    # GoldGenerator().create_item().open() - Вызываем конструктор продукта

    # Создаем генератор случайного количества разных видов продукта
    generators = [GoldGenerator(), GemGenerator(), SilverGenerator(), DiamondGenerator(),
                  PlatinumGenerator(), RubyGenerator(), EmeraldGenerator(), OpalGenerator()]
    for i in range(20):
        generators[randint(0,7)].create_item().open()