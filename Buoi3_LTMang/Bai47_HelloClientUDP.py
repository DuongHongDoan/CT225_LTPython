import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hi there\n"
s.sendto(msg.encode('ascii'), ('localhost', 9999))
data, (a, p) = s.recvfrom(1024)
print(data.decode('ascii'))
s.close()