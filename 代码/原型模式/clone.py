# coding=utf-8
# author='HopePower'
# time='2020/8/2 23:05'
import copy


class A(object):

    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):

    def __init__(self):
        super(B, self).__init__()
        self.y = 34

    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print [str(i) for i in (b, c)]
    print [i for i in (b, c)]