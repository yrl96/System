import socket
import struct
import json
import time

IP_PORT = ('127.0.0.1', 8080)
BufferSize = 1024

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 获取socket对象，并设置通过TCP协议通信
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置连接重用
tcp_server_socket.bind(IP_PORT)  # 绑定IP地址和端口
tcp_server_socket.listen()  # 监听，可指定数量

conn, addr = tcp_server_socket.accept()  # 建立连接
print('client ip addr:', addr)
head_struct = conn.recv(4)  # 接收定制报头的长度
head_json_len = struct.unpack('i', head_struct)[0]  # 解包，获取定制报头的长度
head_json = conn.recv(head_json_len).decode('utf-8')  # 根据上一步解包获得的报头长度，接收报头
head = json.loads(head_json)  # 将json字符串类型的报头转化为python对象
file_size = head['file_size']  # 获取待接收文件的大小
file_name = head['file_name']  # 获取接收文件的名字
print(time.strftime('%Y-%m-%d %H:%M:%S'), ' 开始接收文件...')  # 打印开始接收文件的时间
with open(file_name, 'wb') as f:  # 以二进制写方式打开文件
    '''
    循环写入接收的文件内容
    '''
    while True:
        if file_size >= BufferSize:  # 如果接收的文件内容大于设置的BufferSize，就只接收BufferSize大小的内容
            content = conn.recv(BufferSize)  # 接收客服端发送的BufferSize大小的内容
            f.write(content)  # 在服务端写入BufferSize大小的内容
            file_size -= BufferSize  # 将待写入的文件大小减去已接收的BufferSize大小
            '''
            主要是用于服务端和客户端在同一PC上，且写入比读取快，从而导致服务端先行关闭，
            造成客户端连接中断，文件传送不完整
            '''
            time.sleep(0.00001)
        else:
            content = conn.recv(file_size)  # 接收文件剩余部分
            f.write(content)
            break
print(time.strftime('%Y-%m-%d %H:%M:%S'), ' 成功接收文件...')  # 打印文件接收完成时间

conn.close()  # 关闭连接
tcp_server_socket.close()  # 关闭服务端socket
