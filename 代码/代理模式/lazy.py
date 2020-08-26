# coding=utf-8
# author='HopePower'
# time='2020/8/7 22:41'

class LazyProperty(object):

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print 'function overriden: {}'.format(self.method)
        print 'function\'s name: {}'.format(self.method_name)

    def __get__(self, instance, owner):
        if not instance:
            return None
        value = self.method(instance)
        print 'value {}'.format(value)
        setattr(instance, self.method_name, value)
        return value


class Test(object):

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty # resource = LazyProperty(resource)
    def resource(self):
        print 'initializing self._resource which is: {}'.format(self._resource)
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print t.x
    print t.y
    print t.resource
    print t.resource


if __name__ == '__main__':
    main()