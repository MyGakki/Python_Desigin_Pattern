# coding=utf-8
# author='HopePower'
# time='2020/8/6 22:37'

from abc import ABCMeta, abstractmethod
from enum import Enum

class State(Enum):
    NEW = 'NEW'
    RUNNING = 'RUNNING'
    SLEEPING = 'SLEEPING'
    RESTART = 'RESTART'
    ZOMBIE = 'ZOMBIE'

class Server(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        self.name = 'FileServer'
        self.state = State.NEW

    def boot(self):
        print 'booting the {}'.format(self)
        self.state = State.RUNNING

    def kill(self, restart=True):
        print 'Killing {}'.format(self)
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_file(self, user, name, permissions):
        print "trying to create the file '{}' for user '{}' " \
              "with permissions {}".format(name, user, permissions)


class ProcessServer(Server):

    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.NEW

    def boot(self):
        print 'booting the {}'.format(self)
        self.state = State.RUNNING

    def kill(self, restart=True):
        print 'Killing {}'.format(self)
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_process(self, user, name):
        print "trying to create the process '{}' for user '{}'".format(name, user)


class OperatingSystem:

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)
