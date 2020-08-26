# coding=utf-8
# author='HopePower'
# time='2020/8/7 23:35'

class SensitiveInfo(object):

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print 'There are {} users: {}'.format(len(self.users), ' '.join(self.users))

    def add(self, user):
        self.users.append(user)
        print 'Added user: {}'.format(user)


class Info(object):

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = raw_input('what is the secret?')
        if sec == self.secret:
            self.protected.add(user)
        else:
            print 'That\'s wrong'


def main():
    info = Info()
    while True:
        print '1, read list |==| 2.add user |==| 3.quit'
        key = raw_input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = raw_input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print 'unknown option: {}'.format(key)


if __name__ == '__main__':
    main()


