import socket

localName = socket.gethostname()
print("Ten may tinh cuc bo la:", localName)

ipGG = socket.gethostbyname('www.google.com')
print("Dia chi IP cua google la:", ipGG)

IPAddress = "192.168.103.11"
IPName = socket.gethostbyaddr(IPAddress)
print("Ten cua may co IP {0} la: {1}".format(IPAddress,IPName))

ipGG = socket.gethostbyname(localName)
print("Dia chi IP cua local la:", ipGG)