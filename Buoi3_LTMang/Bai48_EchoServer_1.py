import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 7777))
s.listen(5)
c, (a, p) = s.accept()
print("Connect from ", a)
while True:
    data = c.recv(1024).decode('ascii')
    if not data:
        break
    print(data)
    c.sendall(data.encode('ascii'))
    if data == '#quit':
        break
s.close()