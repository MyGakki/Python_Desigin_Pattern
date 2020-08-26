# coding=utf-8
# author='HopePower'
# time='2020/8/17 0:01'
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Boiler(object):

    def __init__(self):
        self.temperature = 83

    def __str__(self):
        return 'boiler temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print "increasing the boiler's temperature by {} degrees".format(self.temperature)
        self.temperature += amount

    def decrease_temperature(self, amount):
        print "decreasing the boiler's temperature by {} degrees".format(self.temperature)
        self.temperature -= amount


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(word)
    event = command + token + device + Optional(token + argument)

    boiler = Boiler()
    print boiler

if __name__ == '__main__':
    main()