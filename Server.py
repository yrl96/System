import socket
HOST = '127.0.0.1'

PORT = 8888
 
server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print(f'服务器正在监听 {HOST}:{PORT}')
print('正在等待连接...')
conn, addr = server.accept()
print(f'连接成功 addr={addr}')
print('等待消息')
while True:
    msg = conn.recv(1024)
    print('客户端回复:', msg.decode())
    response = input('执行命令>>>')
    conn.send(response.encode())
    print('等待回复')
