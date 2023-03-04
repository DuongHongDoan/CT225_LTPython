f = open("D:\python.txt", "r")
listFile = f.readlines()
lis = listFile[:4]
for i in lis:
    print(i)
f.close()