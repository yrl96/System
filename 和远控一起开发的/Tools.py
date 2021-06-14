import os
import sys

Arg = sys.argv[1: ]


class Main:
    def open(self, URL):
        os.system('start'+' ' + URL)

    def cmd(self):
        os.system('cd C:\\Users\\Administrator\\Desktop\\Work\\Python\\连晨曦\\远控\\ & start cmd')


Main = Main()
if Arg[0] == 'cmd':
    Main.cmd()
elif Arg[0] == 'open':
    Main.open(Arg[1])
else:
    print('...')
