import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

while True:
    data, (a, p) = s.recvfrom(1024)
    print("ServerUDP nhan ket noi tu", a)
    msg = "Hello %s" %a
    s.sendto(msg.encode('ascii'), (a, p))