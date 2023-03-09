import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(1)

while True:
    cli, (remhost, remport) = s.accept()
    print("Nhan ket noi tu", remhost)
    msg = "Hello %s\n" %remhost
    cli.send(msg.encode('ascii'))
    cli.close()