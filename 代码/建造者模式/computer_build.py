# coding=utf-8
# author='HopePower'
# time='2020/8/2 17:28'

#另一个选择是购买一台定制的PC。假若这样，使用的即是建造者模式。
#你是指挥者，向制造商（建造者）提供指令说明心中理想的电脑规格
class Computer:

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

class ComputerBuilder:

    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class HardwareEngineer:

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=500, gpu='GeForce RTX 2080Ti')
    computer = engineer.computer
    print computer

if __name__ == '__main__':
    main()