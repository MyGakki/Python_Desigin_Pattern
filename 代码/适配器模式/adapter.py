# coding=utf-8
# author='HopePower'
# time='2020/8/6 21:39'

from external import Synthesizer, Human

class Computer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play, name=synth.name)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak, name=human.name)))

    for i in objects:
        print '{} {} name:{}'.format(str(i), i.execute(), i.name)


if __name__ == '__main__':
    main()