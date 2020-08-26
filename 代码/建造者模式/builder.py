# coding=utf-8
# author='HopePower'
# time='2020/8/2 17:37'

from enum import Enum
import time

class PizzaProgress(Enum):
    queued = 1
    preparation = 2
    baking = 3
    ready = 4

class PizzaDough(Enum):
    thin = 'thin'
    thick = 'thick'

class PizzaSauce(Enum):
    tomato = 1
    creme_fraiche = 2

class PizzaTopping(Enum):
    mozzarella = 1
    double_mozzarella = 2
    bacon = 3
    mushrooms = 4
    red_onion = 5
    oregano = 6
    ham = 7

STEP_DELAY = 3

class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print '{}正在准备面团{}'.format(self, self.dough)
        time.sleep(STEP_DELAY)
        print '{}面团准备完毕'.format(self.dough)


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print '给你的Margarita披萨添加番茄调味料'
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print '添加番茄调味料完毕'

    def add_topping(self):
        print '给你的Margarita披萨添加奶酪，牛至配料'
        self.pizza.topping.append([i for i in
                                   (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print "添加奶酪，牛至配料完毕"

    def bake(self):
        self.progress = PizzaProgress.baking
        print '烘焙你的Margarita披萨{}秒'.format(self.baking_time)
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print "你的Margarita披萨准备好了"

class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print '给你的CreamyBacon披萨添加法式鲜奶油调味料'
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print '添加法式鲜奶油调味料完毕'

    def add_topping(self):
        print '给你的CreamyBacon披萨添加奶酪，熏肉，火腿，蘑菇，洋葱，牛至配料'
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                    PizzaTopping.ham, PizzaTopping.mushrooms,
                                    PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print '添加奶酪，熏肉，火腿，蘑菇，洋葱，牛至配料完毕'

    def bake(self):
        self.progress = PizzaProgress.baking
        print '烘焙你的CreamyBacon披萨{}秒'.format(self.baking_time)
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print "你的CreamyBacon披萨准备好了"


class Waiter:

    def __init__(self):
        self.builder = None

    def consturct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = raw_input('你想要哪种披萨，[m]argarita or [c]reamy bacon?')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print '只有margarita (key m) 和 creamy bacon (key c)可供选择'
        return (False, None)
    return (True, builder)

def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print ''
    waiter = Waiter()
    waiter.consturct_pizza(builder)
    pizza = waiter.pizza
    print ''
    print '享用你的{}'.format(pizza)


if __name__ == '__main__':
    main()