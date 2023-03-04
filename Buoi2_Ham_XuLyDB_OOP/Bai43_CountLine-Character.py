f = open("D:\python.txt", "r")
cnt = 0
lis = f.read()
line = lis.split("\n")
for i in line:
    cnt += 1
print("So dong trong file la:", cnt)
sum = 0
for i in range(len(lis)):
    if(lis[i]==' ' or lis[i]=='\n'):
        sum += 1
print("So tu trong file la: ", sum)
f.close()