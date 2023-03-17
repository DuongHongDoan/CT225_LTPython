import socket
import threading
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))
helo1 = s.recv(1024)
print("Helo1:", helo1.decode())
ans1 = input()
s.sendall(ans1.encode('ascii'))
helo2 = s.recv(1024)
print("Helo2:", helo2.decode())
def receive():
    while True:
        msg = s.recv(1024).decode('ascii')
        print("Ans:", msg)
recv_thread = threading.Thread(target=receive)
recv_thread.start()
while True:
    msg = input()
    if msg == "#quit":
        break
    s.sendall(msg.encode())
s.close()