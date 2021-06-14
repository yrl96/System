import socket
import struct
import json
import os


def Upload(File_Path, File_Name, IP_PORT=('127.0.0.1', 8080)):
    IP_PORT = IP_PORT
    BufferSize = 1024

    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 获取socket对象
    tcp_client_socket.connect(IP_PORT)  # 连接服务端

    '''
    定制化报头
    '''
    head = {'file_path': File_Path,
            'file_name': File_Name,
            'file_size': 0
            }

    file_path = os.path.join(head['file_path'], head['file_name'])  # 获取要上传文件的完整路径
    file_size = os.path.getsize(file_path)  # 获取文件大小
    head['file_size'] = file_size  # 将获取到的真实文件大小设置到报头

    head_json = json.dumps(head)  # 将报头python对象转化为json字符串
    head_bytes = bytes(head_json, encoding='utf-8')  # 将报头json字符串转化为bytes字节码
    head_struct = struct.pack('i', len(head_bytes))  # 将报头bytes字节码以'integer'类型打包为4个字节
    tcp_client_socket.send(head_struct)  # 发送打包为4个字节的报头
    tcp_client_socket.send(head_bytes)  # 发送定制化报头
    with open(file_path, 'rb') as f:  # 以二进制读的方式打开文件
        '''
        循环读取文件内容并发送给服务端
        '''
        while True:
            if file_size >= BufferSize:  # 如果发送文件的大小大于BufferSize，只读取BufferSize大小的内容
                content = f.read(BufferSize)  # 读取BufferSize大小的内容
                tcp_client_socket.sendall(content)  # 发送读取的文件内容
                file_size -= BufferSize  # 文件大小减去已发送文件的大小
            else:
                content = f.read(file_size)  # 读取剩余文件内容
                tcp_client_socket.sendall(content)  # 发送文件读取的文件内容
                break  # 终止循环

    tcp_client_socket.close()  # 关闭Socket
    return True
