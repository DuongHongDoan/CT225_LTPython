import socket
import threading

Q_ADictionary = {
    u'Ban khoe khong?': 'Minh van khoe. Con ban thi sao ?\n',
    u'Minh khoe, cam on ban nhe!' : 'Khong co gi nhe! ^.^\n',
    u'Ban dang song o dau ?': 'Hien tai tui dang song va hoc tap tai TP.Can Tho\n',
    u'Ban co thich choi the thao khong ?': 'Toi rat thich choi the thao, dac biet la bong ro. Con ban, ban co thich choi bong ro khong ?\n',
    u'Toi rat thich mon the thao do': 'Oh, tuyet voi! :3\n',
    u'Tuong lai ban se lam cong viec gi ?': 'Toi se tro thanh mot lap trinh vien\n',
    u'Toi co viec roi, gap lai ban sau nhe!': 'That tiec! :<\n',
    u'Bye bye!': 'Bai bai'
}

msg = 'Minh dang lang nghe, ban muon noi gi voi minh khong ? :3\n'

def handle_client (c, a, p):
    print("Connect from {0}, tai cong {1}".format(a, p))
    name = 'Donna'
    helo1 = "%s chao ban. Ban ten gi ?" %name
    c.sendall(helo1.encode('ascii'))
    friend = c.recv(1024)
    helo2 = ("Rat vui duoc lam quen voi ban, %s" %friend.decode('ascii'))
    c.sendall(helo2.encode('ascii'))
    while True:
        Q = c.recv(1024)
        # Q = Q[:(len(Q)-2)]
        Q = Q.decode('ascii')
        print(Q)
        print(type(Q))
        A = Q_ADictionary.get(Q, 'unknow')
        print(A)
        if (A != 'unknow'):
            c.sendall(A.encode('ascii'))
        else:
            c.sendall(msg.encode('ascii'))
# Chatbot answer ok, but Error exit !!!
        if (A.encode('ascii') == 'Bai bai'.encode('ascii')):
            continue

        if not Q:
            break
        # print(data)
        # c.sendall(data.encode('ascii'))
        if Q == '#quit':
            break
    c.close()
    return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))
s.listen(5)
while True:
    c, (a, p) = s.accept()
    t = threading.Thread(target=handle_client, args=(c, a, p))
    t.start()