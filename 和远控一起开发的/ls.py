import os
import time
import sys


class lsCommand:

    def default(self):
        __list = os.listdir(os.getcwd())
        for _list in __list:
            print(_list)

    def path(self, pth):
        pth = os.listdir(pth)
        for path in pth:
            print(path)

    def h(self):
        print('''
        指定路径查看 -p Path
        ''')

    def ls(self):
        if not Input:
            ls.default()
        elif Input[0] == '-p':
            ls.path(Input[1])
        elif Input[0] == '-h' or Input[0] == '--help':
            ls.h()


if __name__ == '__main__':
    ls = lsCommand()
    Input = sys.argv[1:]
    ls.ls()
