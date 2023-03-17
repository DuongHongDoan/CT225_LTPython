import socket
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 7777))
while True:
    msg = input()
    s.sendall(msg.encode())
    data = s.recv(1024).decode()
    print("Nhan:", data)
    if msg == "#quit":
        break

s.close()