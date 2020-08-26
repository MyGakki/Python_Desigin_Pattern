# coding=utf-8
# author='HopePower'
# time='2020/8/2 17:16'
# 如果我们知道一个对象必须经过多个步骤来创建，并且要求同一个构造过程可以产生不同的表现，就可以使用建造者模式

#假设你想购买一台新电脑，如果 决定购买一台特定的预配置的电脑型号，例如，最新的苹果1.4GHz Mac mini，则是在使用工厂
#模式。所有硬件的规格都已经由制造商预先确定，制造商不用向你咨询就知道自己该做些什么， 它们通常接收的仅仅是单条指令。
MINI14 = '1.4GHz Max mini'

class AppleFactory:

    class MacMini14:

        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Intel HD Graphics 500'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print 'I don\'t know how to build {}'.format(model)

if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print mac_mini