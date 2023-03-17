import socket
import threading

def handle_client(c, a, p):
    print("Ket noi tu {0}: {1}".format(a,str(p)))
    while True:
        data = c.recv(1024).decode('ascii')
        if not data:
            break
        print(data)
        c.sendall(data.encode('ascii'))
        if data == '#quit':
            break
    c.close()
    return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 7777))
s.listen(1)
while True:
    c, (a, p) = s.accept()
    t = threading.Thread(target=handle_client, args=(c, a, p))
    t.start()