# coding=utf-8
# author='HopePower'
# time='2020/7/27 23:33'


class Frog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print '{} the Frog encounters {} and {}'.format(
            self, obstacle, obstacle.action())


class Bug(object):
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld(object):
    def __init__(self, name):
        print self
        self.player_name = name

    def __str__(self):
        return '\n\n\t -----Forg World-----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print '{} the Wizard battles against {} and {}'.format(
            self, obstacle, obstacle.action())


class Ork(object):
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld(object):
    def __init__(self, name):
        print self
        self.player_name = name

    def __str__(self):
        return '\n\n\t-----Wizard-----'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnivoronment(object):
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validata_age(name):
    try:
        age = raw_input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as err:
        print 'Age {} is invalid, plz try again...'.format(age)
        return False, age
    return True, age

def main():
    name = raw_input('Hello. What''s your name?')
    valid_input = False
    while not valid_input:
        valid_input, age = validata_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnivoronment(game(name))
    environment.play()


if __name__ == '__main__':
    main()