# coding=utf-8
# author='HopePower'
# time='2020/8/9 14:02'

import os

verbose = True


class RenameFile(object):

    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print "[renaming '{}' to '{}']".format(self.src, self.dest)
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print "[renaming '{}' back '{}']".format(self.dest, self.src)
        os.rename(self.dest, self.src)


class CreateFile(object):

    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print "[creating file '{}']".format(self.path)
        with open(self.path, mode='w') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile(object):

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print "[reading file '{}']".format(self.path)
        with open(self.path, mode='r') as in_file:
            print in_file.read()


def delete_file(path):
    if verbose:
        print "[deleting file '{}']".format(path)
    os.remove(path)

def main():
    orgi_name, new_name = './file1', './file2'

    commands = []
    for cmd in CreateFile(orgi_name), ReadFile(orgi_name), RenameFile(orgi_name, new_name):
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = raw_input('reverse the executed commands?[y/n]')

    if answer not in 'yY':
        print 'the result is {}'.format(new_name)
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == '__main__':
    main()
