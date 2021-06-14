# coding=utf-8
import os
import time
from pythonping import ping
from io import StringIO
import ast
import json
from psutil import disk_partitions
import sys
import wget
import random
import codecs
import shutil


# 关于
def Copyright():
    __Author = 'YangWeb'
    __ProductionTime = '2021/6/12'
    __Line = 'I don`t know'


# 系统内存
class Memory:
    # 内存地址
    def __init__(self):
        # None is not defined
        # True is all can read
        # False is all can`t read
        self.MemoryState = None
        self.MemoryAddress = {'0x0000': False, '0x0001': None, '0x0010': None, '0x0011': None, '0x0100': None,
                              '0x0111': None,
                              '0x1000': None, '0xFFFF': '5p2o5L2z5piK'}

    # 读内存的API
    def ReadMemory(self, Address):
        if Memory.MemoryState is False:
            return False
        else:
            pass
        if Address in Memory.MemoryAddress:
            if Address == '0x0000' or Address == '0xFFFF':
                return None
            else:
                return Memory.MemoryAddress[Address]

    # 写内存的API
    def WriteMemory(self, Word):
        if Memory.MemoryState is False:
            return False
        else:
            pass
        Memory.MemoryAddress['0x0001'] = Word

        return '0x0001'

    # 内存回收
    def MemoryFree(self):
        Memory.MemoryState = False
        del Memory.MemoryAddress


# 内核部分
class Kernel:

    # 初始化变量
    def __init__(self):
        # 登录状态
        self.Login = 0
        # 目录(已弃用)
        self.Catalogue = ['usr', 'tmp', 'etc', 'dev', 'home']
        # 功能
        self.Function = ['ls', 'cd', 'vi', 'ping', 'logout', 'help', 'gettime', 'init 0', 'passwd', 'usblist', 'wget',
                         'rm', 'selfstart', 'delstart', 'copy']
        # 启动状态
        self.Start = False
        # 初始化内存
        self.Mem = StringIO()
        self.Word = None
        # 清理内存次数
        self.INIT = 0
        self.Language = None
        self.IO = False
        self.Sdc = None
        self.OEM = {'User': None, 'RandomNumber': random.randint(1000, 9999), 'CopyRight': 'YangWeb'}
        # 版本
        self.Version = 'Doge OS 5.0'
        self.LanguageSelect = None
        self.L = None
        self.Self = None

    # 函数描述
    def __str__(self):
        return None

    # 写入内存
    def MemWrite(self, Word):
        Kernel.Word = str(Word)
        Kernel.Mem.write(Kernel.Word)

    # 读取内存
    def MemRead(self):
        return Kernel.Mem.getvalue()

    # 启动
    def Boot(self):
        Kernel.Examine()
        Memory.WriteMemory('title DogeOS')
        if Kernel.L is None:
            exit()
        else:
            pass
        Languages.LanguageRead()
        if not Kernel.IO:
            exit()
        else:
            pass
        if Kernel.LanguageSelect[0] is True:
            Languages.CN()
        else:
            Languages.LanguageLoad()
        Kernel.Start = True
        print(Kernel.Language[0])
        print(Kernel.Language[1])
        time.sleep(1)
        print(Kernel.Language[2])
        print(Kernel.Language[3])
        Kernel.MemWrite(Kernel.Function)
        os.system('cls')
        os.system(Memory.ReadMemory('0x0001'))
        Kernel.SelfStart()

    # 内存清理
    def init(self):
        if Kernel.INIT == 1:
            return None
        else:
            pass
        del Kernel.Word
        del Kernel.Mem
        Memory.MemoryFree()
        Kernel.INIT = 1

    # 系统文件校验
    def Examine(self):
        ii = 0
        for i in os.listdir():
            if i == 'System.bin':
                ii += 1
            else:
                pass
        if ii == 0:
            exit()
        else:
            pass
            aa = 0
            for a in os.listdir():
                if a == 'EN.bin':
                    Kernel.IO = True
                    aa += 1
                else:
                    pass
            if aa == 0:
                pass
            else:
                pass
        ss = 0
        for List in os.listdir():
            if List == 'CN.py':
                ss += 1
                Kernel.IO = True
            else:
                pass
        dd = 0
        for Lists in os.listdir():
            if Lists == 'Language.bin':
                dd += 1
                Kernel.L = True
            else:
                pass

    def SelfStartWrite(self, Command):
        for a in os.listdir():
            if a == 'SelfStart.bin':
                os.remove('SelfStart.bin')
            else:
                pass
        for i in Kernel.Function:
            if i == Command:
                Write = json.dumps([Command])
                File = open('SelfStart.bin', 'w')
                File.write(Write)
                File.close()
            else:
                pass

    def SelfStart(self):
        try:
            File = open('SelfStart.bin', 'r')
            F = json.loads(File.read())
            Kernel.Self = F
            File.close()
        except:
            pass
        else:
            pass

    def SStart(self):
        if Kernel.Self is None:
            return None
        FunctionNumber = None
        for i in range(len(Kernel.Function)):
            if Kernel.Function[i] == Kernel.Self[0]:
                FunctionNumber = i
            else:
                pass
        if FunctionNumber is None:
            pass
        else:
            Run(FunctionNumber)


# 语言部分
class Languages:
    # 老init了
    def __init__(self):
        pass

    # 懒得写
    def __str__(self):
        pass

    # 语言读取
    def LanguageRead(self):
        Language = open('Language.bin', 'r')
        L = Language.read()
        L = json.loads(L)
        Kernel.LanguageSelect = L
        Language.close()

    # 加载中文
    def CN(self):
        try:
            import CN
            Kernel.Language = CN.CN
        except:
            pass
        else:
            pass

    # 加载英语
    def LanguageLoad(self):
        LanguageEn = open('EN.bin', 'r')
        English = LanguageEn.read()
        English = json.loads(English)
        Kernel.Language = English
        LanguageEn.close()


# 功能部分
class Main:
    # 我就是要水代码,欧耶
    def __init__(self):
        self.Str = 'Main'

    def __str__(self):
        return Main.Str

    # 同windows的dir
    def ls(self, Dir=None):
        if Dir is None:
            List = os.listdir()
            if 'System.bin' in List:
                List.remove('System.bin')
            if 'EN.bin' in List:
                List.remove('EN.bin')
            if 'CN.py' in List:
                List.remove('CN.py')
            if 'Language.bin' in List:
                List.remove('Language.bin')
            for i in List:
                print(i)
        else:
            try:
                List = os.listdir(Dir)
                if 'System.bin' in List:
                    List.remove('System.bin')
                    List.remove('EN.bin')
                for i in List:
                    print(i)
            except:
                print(Kernel.Language[4])
            else:
                pass

    # 最后决定使用实体目录
    # 同windows的cd
    def cd(self, Dir=None):
        if Dir is None:
            print(os.getcwd())
        else:
            try:
                os.chdir(Dir)
            except:
                print(Kernel.Language[5])
            else:
                pass

    # 同windows的ping(不是win32api)
    def ping(self, IP=None):
        if IP is None:
            print(Kernel.Language[6])
        else:
            try:
                print(ping(IP))
            except:
                print(Kernel.Language[7])
            else:
                pass

    # 帮助(输出所有命令)
    def Help(self):
        for i in Kernel.Function:
            print(i)

    # 当前时间
    def Time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 关机
    def Logout(self):
        print(Kernel.Language[8])
        if Kernel.INIT == 1:
            pass
        else:
            del Kernel.Word
            del Kernel.Mem
            Memory.MemoryFree()
        time.sleep(2)
        exit()

    # 笑死,根本做不了
    def vi(self):
        print(Kernel.Language[9])
        time.sleep(5)
        print(Kernel.Language[10])

    # 改密码
    def UserUpdate(self, ReadOrWrite):
        if ReadOrWrite == 'Write':
            IO = False
            for i in os.listdir():
                if i == 'System.bin':
                    IO = True
                else:
                    pass
            if IO is True:
                os.remove('System.bin')
            else:
                pass
            UsrPwd = [Bash.User, Bash.PassWord]
            UsrAndPwd = json.dumps(UsrPwd)
            File = open('System.bin', 'w')
            File.write(UsrAndPwd)
            File.close()
        elif ReadOrWrite == 'Read':
            File = open('system.bin', 'r')
            UsrPwd = File.read()
            UserAndPwd = json.loads(UsrPwd)
            File.close()
            return UserAndPwd

    # U盘盘符查看
    def Dev(self):
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                Kernel.Sdc = driver
            else:
                pass

    # 下载文件
    def Wget(self, URL=None, FileName=None):
        if URL is None:
            return None
        else:
            if FileName is None:
                try:
                    wget.download(URL)
                except:
                    print(Kernel.Language[22])
                else:
                    print(Kernel.Language[26])
            else:
                try:
                    wget.download(URL, out=FileName)
                except:
                    print(Kernel.Language[22])
                else:
                    print(Kernel.Language[26])

    # 删除文件
    def rm(self, FileName=None):
        if FileName is None:
            print('???')
        else:
            try:
                os.remove(FileName)
            except:
                print(Kernel.Language[27])
            else:
                pass

    def copy(self, Src, Dst):
        try:
            shutil.copy(Src, Dst)
        except:
            print(Kernel.Language[30])
        else:
            pass


# 命令链接
# 启动器
def Run(Number):
    # 亿些条件判断
    # 查看目录下文件
    if Number == 0:
        Route = input(Kernel.Language[11])
        if Route == '':
            Main.ls()
        else:
            Main.ls(Route)
    # 切换目录
    elif Number == 1:
        CdRoute = input(Kernel.Language[11])
        if len(CdRoute) == 0:
            Main.cd()
        else:
            Main.cd(CdRoute)
    # 退出登录
    elif Number == 4:
        Main.Logout()
    # Ping
    elif Number == 3:
        PingIP = input(Kernel.Language[12])
        Main.ping(PingIP)
    # 帮助
    elif Number == 5:
        Main.Help()
    # 时间
    elif Number == 6:
        print(Main.Time())
    # 清理内存
    elif Number == 7:
        Kernel.init()
    # 根本没做vi
    elif Number == 2:
        Main.vi()
    # 密码修改
    elif Number == 8:
        Usr = input(Kernel.Language[13])
        if Usr == Bash.User:
            pass
        else:
            return None
        Pwd = input(Kernel.Language[14])
        if Pwd == Bash.PassWord:
            NewPass = input(Kernel.Language[15])
            if len(NewPass) > 0:
                Bash.PassWord = NewPass
                Main.UserUpdate('Write')
    # 查看U盘盘符
    elif Number == 9:
        Main.Dev()
        if Kernel.Sdc is None:
            print(Kernel.Language[21])
        else:
            print(Kernel.Language[23], Kernel.Sdc)
            Kernel.Sdc = None
    # 下载文件
    elif Number == 10:
        URL = input(Kernel.Language[24])
        FileName = input(Kernel.Language[25])
        Main.Wget(URL, FileName)

    # 删除文件
    elif Number == 11:
        FileNames = input(Kernel.Language[28])
        if len(FileNames) == 0:
            Main.rm()
        else:
            Main.rm(FileNames)
    elif Number == 12:
        BASH = input(Kernel.Language[29])
        if len(BASH) == 0:
            pass
        else:
            Kernel.SelfStartWrite(BASH)
    elif Number == 13:
        for sb in os.listdir():
            if sb == 'SelfStart.bin':
                os.remove('SelfStart.bin')
            else:
                pass
    elif Number == 14:
        FileName = input('FileName:')
        To = input('To:')
        Main.copy(FileName, To)


# 终端
class Bash:
    # 声明变量
    def __init__(self):
        File = open('System.bin', 'r')
        FileR = File.read()
        Word = json.loads(FileR)
        File.close()
        self.User = Word[0]
        self.PassWord = Word[1]

    def __str__(self):
        return 'Bash'

    # 登录
    def Login(self):
        if Kernel.Login is True:
            pass
        else:
            pass
        while True:
            UserName = input(Kernel.Language[16])
            if UserName == Bash.User:
                pass
            else:
                print(Kernel.Language[17])
                continue
            UserPass = input(Kernel.Language[18])
            if UserPass == Bash.PassWord:
                Kernel.Login = 1
                break
            else:
                print(Kernel.Language[19])
                continue

    # 主程序
    def Main(self):
        MemoryFunction = ast.literal_eval(Kernel.MemRead())
        if Kernel.Login == 1:
            pass
        else:
            print(Kernel.Language[20])
            exit()
        Welcome = 0
        while True:
            if Welcome == 0:
                Welcome += 1
                print('---------------'
                      '|   Welcome   |'
                      '--------------')
            else:
                pass
            Input = input('root@YangWeb~#')
            Functions = len(MemoryFunction)
            FunctionNumber = None
            for i in range(Functions):
                if MemoryFunction[i] == Input:
                    FunctionNumber = i
                else:
                    pass
            if FunctionNumber is None:
                pass
            else:
                Run(FunctionNumber)


# 安装程序
class Setup:
    def __init__(self):
        self.NamePwd = None
        self.IO = None
        self.Str = 'Setup'
        self.KeyInput = None

    def __str__(self):
        return Setup.Str

    # 秘钥
    def Key(self):
        Key = input('Please Input Your`s Key:')
        if len(Key) == 0:
            print('Ask your system administrator for a key')
            exit()
        else:
            if Key == '20080522':
                print('The Key is successful')
                Setup.KeyInput = True
            elif Key == '6L+e5pmo5pum':
                print('What?!')
                Setup.KeyInput = True
            elif Key == '5p2o5L2z5piK':
                print('......Who....is you?')
                Setup.KeyInput = True
            else:
                exit()

    # 一些校验
    def Set(self):
        IO = None
        IOA = None
        IOB = None
        IOC = None
        for i in os.listdir():
            if i == 'System.bin':
                IO = True
            else:
                pass
            if i == 'EN.bin':
                IOA = True
            else:
                pass
            if i == 'CN.py':
                IOB = True
            else:
                pass
            if i == 'Language.bin':
                IOC = True
            else:
                pass
        if IO is True:
            os.remove('System.bin')
        else:
            pass
        if IOA is True:
            os.remove('EN.bin')
        else:
            pass
        if IOB is True:
            os.remove('CN.py')
        else:
            pass
        if IOC is True:
            os.remove('Language.bin')

    # 写入用户
    def User(self):
        if Setup.KeyInput is None:
            exit()
        else:
            pass
        while True:
            UserName = input('UserName:')
            PassWord = input('PassWord:')
            if len(UserName) == 0 or len(PassWord) == 0:
                continue
            else:
                break
        Bash.User = UserName
        Bash.PassWord = PassWord
        Main.UserUpdate('Write')
        L = input('Please choose your Language(CN or EN):')
        if L == 'CN':
            Setup.LanguageCN(True)
            Setup.CN()
        else:
            Setup.LanguageCN(False)
            Setup.Language()

    # 写入语言资源
    def Language(self):
        EN = ['Starting.', 'Starting...', '[INFO]Loading ACPI', '[Success]StartOS', 'Not have this route',
              'Not have this path', 'Ip must be specified', 'I can`t ping this ip address', 'Shutdown...',
              'Please wait...', '(:>Your computer has a problem and needs to be restarted', 'Route:', 'IP:',
              'Please input your UserName', 'PassWord:', 'New PassWord:', 'UserName:', 'UserNameError', 'PassWord:',
              'PassWordError', 'Illegal Login', 'Not USB', 'DownLoadError', 'USB is in', 'URL:', 'FileName:', 'Success',
              'File Not Found', 'Command:', 'Error']
        Write = json.dumps(EN)
        File = open('EN.bin', 'w')
        File.write(Write)
        File.close()

    # 读取语言选择
    def LanguageCN(self, Language=None):
        Language = [Language]
        Write = json.dumps(Language)
        File = open('Language.bin', 'w')
        File.write(Write)
        File.close()

    # 写入中文
    def CN(self):
        CN = "CN = ['启动中.', '正在启动...', '[INFO]加载变量', '[Success]启动成功', '没有这个目录','没有这个地址', 'IP不合法', 'Ping失败', '关机中...','请等待...', '(:>你的电脑遇到问题,需要重新启动', '目录:', 'IP:','请输入你的用户名:', '密码:', '新密码:', '用户名:', '用户名错误', '密码:', '密码错误', '非法登录', '没有USB设备', '下载失败', 'USB在', 'URL:', '文件名:', '成功', '找不到文件', '命令:', '错误']"
        F = codecs.open('CN.py', 'w', 'utf-8')
        F.write(CN)
        F.close()


# 调用,启动系统
if __name__ == "__main__":
    Memory = Memory()
    Languages = Languages()
    Kernel = Kernel()
    Main = Main()
    Setup = Setup()
    parameter = sys.argv
    if len(parameter) > 1 and parameter[1] == '-setup':
        Setup.Set()
        Setup.Key()
        Setup.User()
        print('OK!')
    elif len(parameter) > 1 and parameter[1] == '-install':
        Setup.Set()
        Setup.Key()
        Setup.User()
        print('OK!')
    else:
        Bash = Bash()
        Kernel.Boot()
        Bash.Login()
        Kernel.SStart()
        Bash.Main()
